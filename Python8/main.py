### Import Libraries
import sys
import pandas as pd
import numpy as np
from pathlib import Path
from sqlalchemy import create_engine
import warnings
from pyspark.sql import SparkSession
import pyspark
import glob
import os
from pyspark.sql.functions import col
from pyspark.sql import functions as func
from pyspark.sql import functions as F
from pyspark.sql.functions import *
from datetime import datetime
from datetime import timezone
from pyspark.sql.types import StructType
from pyspark.sql.functions import monotonically_increasing_id, row_number
from pyspark.sql import Window
import warnings
####End of importing libraries

warnings.filterwarnings("ignore")

pathCurrrent = Path.cwd()
pathCurrrent = str(pathCurrrent).replace("\\", '/')
pathData= pathCurrrent + "/data/all/"

# Create spark session
spark = SparkSession.builder.appName('PySpark Read CSV').getOrCreate()

all_files = glob.glob(os.path.join(pathData , "*.csv"))


# Create a dictionary of collection of csv files
frames = {}

for index, csvPath in enumerate(all_files):

    df = spark.read.csv(csvPath)

    for i in range (len(df.columns)):
        df=df.withColumnRenamed(df.columns[i], list(df.head(1)[0])[i])

    frames[all_files[index].split("\\")[1]] = df



# Read each dataset from dictionary of datasets

listOfDF=[]
listOfDevice1=[]
listOfDevice2=[]

for key, item in zip(frames.keys(), frames.items()):

    # Remove first line that include reduntent name of columns
    dfNoHeader = item[1].filter(item[1].DeviceID !='DeviceID')

    print(f"\n Dataset Name: {key}: \n")

    print("++++++++++++++++++++++++ \n")

    print('\n Dataset Schema: {key}: \n')
    print(dfNoHeader.printSchema())


    print(dfNoHeader.show(5))

    # Doing a few cleaning approaches
    print('na rows removed:')
    dfNoHeader.na.drop().show()


    # Drop rows having null values
    dropNa1 = dfNoHeader.dropna()


    # Drop duplicate rows means drop similar rows and take one of them
    print('duplicate rows removed:')
    dropDuplicates1 = dropNa1.dropDuplicates()
    dropDuplicates1.dropDuplicates().show()


    # Drop duplicate rows having similar values in columns ['DeviceID','DataSourceID','SiteID','Timestamp','Metric']
    dropDuplicates2 = dropDuplicates1.orderBy('DeviceID').dropDuplicates(subset = ['DeviceID','DataSourceID','SiteID','Timestamp','Metric'])


    # Drop rows having Metric with value "error"
    dropError = dropDuplicates2.filter(dropDuplicates2.Metric != "error")
    print('Drop rows including Metric with error value:')
    dropError.show(20)


    # Cast ProcessingTimestamp to normal time format
    dropError.select(dropError.ProcessingTimestamp.cast('timestamp')).show(truncate= False)



    # Cast Timestamp and ProcessingTimestamp to normal time format
    # Substract time of Timestamp to ProcessingTimestamp and calulate second differences
    print(f'DiffInSeconds:')
    diffTimeSec = dropError.withColumn('Timestamp', to_timestamp(col('Timestamp'))) \
    .withColumn('ProcessingTimestamp', to_timestamp(col('ProcessingTimestamp'))) \
    .withColumn('DiffInSeconds', col("Timestamp").cast("long") - col('ProcessingTimestamp').cast("long"))



    # All ProcessingTimestamp values are bigger that Timestamp values
    diffTimeSecMinus = diffTimeSec.filter(diffTimeSec.DiffInSeconds < 0)


    # Cast ProcessingTimestamp to normal time
    hours = diffTimeSecMinus.select(diffTimeSecMinus.ProcessingTimestamp.cast('timestamp'))
    hours = hours.withColumnRenamed(hours.columns[0], 'hours')


    # add 'sequential' index and join both dataframe to get the final result
    diffTimeSecMinus = diffTimeSecMinus.withColumn("row_idx", row_number().over(Window.orderBy(monotonically_increasing_id())))
    hours = hours.withColumn("row_idx", row_number().over(Window.orderBy(monotonically_increasing_id())))


    # Join dataframe with one column as hour with main dataframe as diffTimeSecMinus
    print('concat two tables')
    final_df = diffTimeSecMinus.join(hours, diffTimeSecMinus.row_idx == hours.row_idx).drop("row_idx")
    final_df.show(5, truncate=True)


    # Take hours of ProcessingTimestamp values
    dfHours = final_df.withColumn('Hours', hour(final_df.hours))

    # Display the result
    dfHours.show(20, False)



    # Filter data with conditions of Task3
    dfFilter1 = dfHours.filter(col("DeviceType").contains("Inverter") & col("Metric").contains("ac_active_power"))
    print('\n dfFilter1 result:\n')
    dfFilter1.show(20, truncate=True)



    # Answer of last part Task 1
    dfDeviseTask1= dfFilter1.filter(col("DeviceID").contains("1054530426") & col("Timestamp").contains("2021-11-04 11:00:00"))
    dfGroupByDeviseTask1 = dfDeviseTask1.groupby('DeviceID', 'DataSourceID', 'SiteID', 'DeviceType').agg(
        {"hours": 'mean', "Metric": 'count'})

    print("Device 1054530426:")
    dfGroupByDeviseTask1.show()

    dfGroupByDeviseTask1_2PD = dfGroupByDeviseTask1.toPandas()
    listOfDevice1.append(dfGroupByDeviseTask1_2PD)


    # Groupby data with conditions of Task3
    dfGroupBy1 = dfFilter1.groupby('DeviceID','DataSourceID','SiteID','DeviceType').agg({"hours": 'mean', "Metric": 'count'})


    # Convert data to pandas dataframe to be prepared for creating CSV results and append to the list as listOfDF
    dfGroupBy1_2PD = dfGroupBy1.toPandas()
    listOfDF.append(dfGroupBy1_2PD)


    print(f'\n dfGroupBy1 result_{key}:\n')
    dfGroupBy1.show(truncate=True)

    # Filter data to answer last part of Task3
    dfGroupBy1.filter(col("DeviceID").contains("1054530426")).show()





    # Filter data with conditions of Task4
    dfFilter2 = dfHours.filter(col("DeviceType").contains("Sensor") & col("DeviceType").contains("Satellite") &  col("Metric").contains("irradiance"))

    print(f'\n dfFilter2 result_{key}\n')
    dfFilter2.show(truncate=True)



    # Answer of last part Task 2
    dfDeviseTask2 = dfFilter2.filter(col("DeviceID").contains("1054530426") & col("Timestamp").contains("2021-11-04 11:00:00"))
    dfGroupByDeviseTask2 = dfDeviseTask2.groupby('DeviceID', 'DataSourceID', 'SiteID', 'DeviceType').agg(
        {"hours": 'mean', "Metric": 'count'})

    print("Device 3258837907:")
    dfGroupByDeviseTask2.show()

    dfGroupByDeviseTask2_2PD = dfGroupByDeviseTask2.toPandas()
    listOfDevice2.append(dfGroupByDeviseTask2_2PD)





    # Groupby data with conditions of Task4
    dfGroupBy2 = dfFilter2.groupby('DeviceID', 'DataSourceID', 'SiteID', 'DeviceType').agg({"hours": 'mean', "Metric": 'count'})


    # Convert data to pandas dataframe to be prepared for creating CSV results and append to the list as listOfDF
    dfGroupBy2_2PD = dfGroupBy2.toPandas()
    listOfDF.append(dfGroupBy2_2PD)



    print(f'\n dfGroupBy2 result_{key}\n')
    dfGroupBy2.show(truncate=True)

    # Filter data to answer last part of Task4
    dfGroupBy2.filter(col("DeviceID").contains("3258837907")).show()



# Concatenate list of Dataframe results for each CSV file
dfs = pd.concat(listOfDF)


# Answer of last part Task 1
dfDevice1 = pd.concat(listOfDevice1)
print(f"\n All listOfDevice1: {listOfDevice1} \n")


# Answer of last part Task 2
dfDevice2 = pd.concat(listOfDevice2)
print(f"\n All listOfDevice2: {listOfDevice2} \n")


dfAll= pd.concat([dfDevice1, dfDevice2, dfs],axis=0)


# Create 'dfResults.csv'
print('\n dfAllResults.csv was created!')
dfAll.to_csv('dfAllResults.csv', index=None)









