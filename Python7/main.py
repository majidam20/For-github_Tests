# Import libraries
import pandas as pd
import re
import tasks


# Create object from class tasks
salesImp = tasks


# Get database connection information from file connConfigs.txt
dbConfigsFile = "connConfigs.txt"
connConfigs = pd.read_csv(dbConfigsFile, sep=',')



### Task 1.a: print hello + input name
print(f"\n Please enter a name: ")
# Get a name as input
name = input()

print(f"\n Output task1.a: {salesImp.returnName(name)} \n")

outputFile = "outputTask1a.txt"
outputLog = f"\n Output task1.a: {salesImp.returnName(name)} \n"


# Call logOutputs to save log outputs in file outputTask1a.txt
salesImp.logOutputs(outputFile, outputLog)


# Pass connection information to connectToDb function for connecting to the database
dbEngine = salesImp.connectToDb(connConfigs.loc[0,'server'], connConfigs.loc[0,'user'], connConfigs.loc[0,'passw'], connConfigs.loc[0,'port'])

# Insert log outputs to outputTask1a table
tableName= "outputTask1a"
salesImp.insertToDb(dbEngine, connConfigs.loc[0,'dbName'], tableName, outputLog)





### Task 1.b: Sum three numbers
# Enter three numbers from input dialog
print(f"\n Please enter number1: ")

# Ignore charachters in input numbers
number1= float(re.sub('[^0-9\.]', '', input()))

print(f"\n Please enter number2: ")
number2= float(re.sub('[^0-9\.]', '', input()))

print(f"\n Please enter number3: ")
number3= float(re.sub('[^0-9\.]', '', input()))


print(f"\n Output task1.b (Sum three numbers): {salesImp.returnSum(number1, number2, number3)} \n")

outputFile = "outputTask1b.txt"
outputLog = f"\n Output task1.b (Sum three numbers): {salesImp.returnSum(number1, number2, number3)} \n"

# Call logOutputs to save log outputs in file outputTask1b.txt
salesImp.logOutputs(outputFile, outputLog)


# Insert log outputs to outputTask1b table
tableName= "outputTask1b"
salesImp.insertToDb(dbEngine, connConfigs.loc[0,'dbName'], tableName, outputLog)




### Task 1.c:
# Example of a data for iterating through rows and columns:
data = {'Name': ['Majid', 'Hamid', 'Saeed'],
        'Age': [36, 47, 45],
        'Country': ['Iran', 'Italy', 'France']
        }

# Convert example data to DataFrame and read column names
dfData= pd.DataFrame(data)
columns = dfData.columns.values

outputFile = "outputTask1c.txt"
tableName  = "outputTask1c"

# Iterate over rows and columns
# Insert log outputs to outputTask1c.txt and table outputTask1c
salesImp.iterOverCsv (dbEngine, connConfigs.loc[0,'dbName'], tableName,dfData, columns, outputFile)


















