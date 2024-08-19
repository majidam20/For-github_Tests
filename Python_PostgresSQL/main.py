### Import Libraries

import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine
import sqlalchemy
import warnings
####End of importing libraries

warnings.filterwarnings("ignore")

pathCurrrent = Path.cwd()
pathCurrrent = str(pathCurrrent).replace("\\", '/')
pathData = pathCurrrent +"/daily reports/"

# Read csv files by pandas
df_2022_09_16 = pd.read_csv(pathData + "2022-09-16-23-04-01-EDT-Historical-Report-ENTRFacebook-2022-06-17--2022-09-17.csv")
df_2022_09_18 = pd.read_csv(pathData + "2022-09-18-23-03-32-EDT-Historical-Report-ENTRFacebook-2022-06-19--2022-09-19.csv")
df_2022_09_21 = pd.read_csv(pathData + "2022-09-21-23-04-26-EDT-Historical-Report-ENTRFacebook-2022-06-22--2022-09-22.csv")


# Read database configuration from dbConfigs.txt file
dbConfigs = pd.read_csv(pathCurrrent + "/dbConfigs.txt")

# Connect to database with dbConfigs data
engine = create_engine(f"postgresql+psycopg2://{dbConfigs.loc[0,'user']}:{dbConfigs.loc[0,'password']}@{dbConfigs.loc[0,'host']}/{dbConfigs.loc[0,'dbname']}")


# Check If the table already was existed or not
if sqlalchemy.inspect(engine).has_table("df_2022_09_16") == False:

    # Create table and Insert CSV file to database as a new table
    df_2022_09_16.to_sql('df_2022_09_16', con=engine, index=False )
    print("\nData is saved in table df_2022_09_16")

else:
    print("\nTable df_2022_09_16 was already created!")



# Check If the table already was existed or not
if sqlalchemy.inspect(engine).has_table("df_2022_09_18") == False:

    # Create table and Insert CSV file to database as a new table
    df_2022_09_18.to_sql('df_2022_09_18', con=engine, index=False)
    print("\nData is saved in table df_2022_09_18")

else:
    print("\nTable df_2022_09_18 was already created!")


# Check If the table already was existed or not
if sqlalchemy.inspect(engine).has_table("df_2022_09_21") == False:

    # Create table and Insert CSV file to database as a new table
    df_2022_09_21.to_sql('df_2022_09_21', con=engine, index=False)
    print("\nData is saved in table df_2022_09_21")

else:
    print("\nTable df_2022_09_21 was already created!")



# Write some cleaning and transformation on datasets by Python codes
# Delete duplicate rows and keep the first one
df_2022_09_16_cleaned = df_2022_09_16.drop_duplicates(keep="first")

# Delete rows that all columns are null
df_2022_09_16_cleaned = df_2022_09_16_cleaned.dropna(how="all")


# Get sum of Sads in each Page Name groups
dfcount_Sad = df_2022_09_16.groupby(by=["Page Name"])["Sad"].sum().sort_values(ascending=False).reset_index(name="count_Sad")


# Get sum of Total Views in each Page Name groups
dfsum_TotalViews = df_2022_09_16.groupby(by=["Page Name"])["Total Views"].sum().sort_values(ascending=False).reset_index(name="sum_Total Views")


# Get count of Page Admin Top Country in each Page Name and Page Admin Top Country groups
dfcount_PATC = df_2022_09_16.groupby(by=["Page Name","Page Admin Top Country"])["Page Admin Top Country"].count().sort_values(ascending=False).reset_index(name="count_Page Admin Top Country")


# Get count of Post Created Date in each Page Name,Post Created Date groups
dfcount_PCD = df_2022_09_16.groupby(by=["Page Name","Post Created Date"])["Post Created Date"].count().sort_values(ascending=False).reset_index(name="count_Sad")