# Import libraries
import mysql.connector


def connectToDb(server, user, passw, port):
    """
    Receive connection information and connect to database.

    Parameters
    ----------
    conInfoFile : str
                  connection information txt file name.

    Returns
    -------
    dbEngine:   DataBase connection's object
    """
    try:
        db_config = {
        "host": server,
        "user": user,
        "password": f'{passw}',
        "port": port
        }
        dbEngine = mysql.connector.connect(**db_config)

        return dbEngine


    # If connection is not successful
    except:
        print("Can't connect to database!")
        return 0



def insertToDb(dbEngine, dbName, tableName, outputLog):
    """
    Create database and required tables also insert log files to corresponding table.

    Parameters
    ----------
    dbEngine: DataBase connection's object

    dbName:    str
               Database name

    tableName: str
               Table name

    outputLog: str
               Output logs

    """
    conn = dbEngine.cursor()

    # Create a new database if not existed
    sqlQuery= f"CREATE DATABASE IF NOT EXISTS {dbName}"
    conn.execute(sqlQuery)
    conn.execute("commit")


    # Create a new table if not existed
    sqlQuery= f"CREATE table IF NOT EXISTS {dbName}.{tableName} (logs TEXT NULL);"
    conn.execute(sqlQuery)
    conn.execute("commit")


    # Insert to table outputLogs the outputs logs
    sqlQuery= f"INSERT INTO {dbName}.{tableName} (logs) VALUES('{outputLog}');"
    conn.execute(sqlQuery)
    conn.execute("commit")



def logOutputs(outputFile, outputLog):
    """
    Add log outputs into a text file.

    Parameters
    ----------
    outputFile: str
                outputFile name

    outputLog:  str
                Output logs

    """
    with open(outputFile, 'a+') as f:
         f.write(str(outputLog))



# Task 1.a: print hello + input name
def returnName(name):
    return 'Hello ' + name




def returnSum(num1, num2, num3):
    """
    Sum three numbers

    Parameters
    ----------
    num1:  float
           Input number 1

    num2:  float
           Input number 2

    num3:  float
           Input number 3

    Returns
    -------
    A float number : Sum three numbers
    """
    return sum([num1, num2, num3])




def iterOverCsv(dbEngine, dbName, tableName, dfData, columns, outputFile):
    """
    Iterate over rows and columns.
    Call logOutputs to save log outputs in file outputTask1c.txt.
    Insert log outputs to outputTask1c table.

    Parameters
    ----------
    dbEngine : connection objects
               Returned by connectToDb function.

    dbName: str
            Database name

    tableName: str
               Table name

    dfData: DataFrame
            Example of a data considts of rows and columns

    tableName: List of column
               Columns names

    outputFile: str
                outputFile name
    Returns
    -------
    conNameVar: DataBase connection's object
    """

    # Iterate over rows and columns
    for index, row in dfData.iterrows():
        for colName in columns:
            print(f"Row{index}: Column: {colName} Value: {row[colName]} \n")

            # Call logOutputs to save log outputs in file outputTask1c.txt
            outputLog= f"\n Row{index}: Column: {colName} Value: {row[colName]}"
            logOutputs(outputFile, outputLog)

            # Insert log outputs to outputTask1c table
            insertToDb(dbEngine, dbName, tableName, outputLog)