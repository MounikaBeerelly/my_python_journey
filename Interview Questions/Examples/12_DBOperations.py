import mysql.connector as mysql
import os

os.system("cls")

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "localhost",
    database = "employees"
)

myCursor = db.cursor()

# Create new Database
"""
myCursor.execute("CREATE DATABASE Employees")
"""

# show all the available databases
myCursor.execute("SHOW DATABASES")
myDatabases = myCursor.fetchall()
for outDBName in myDatabases :
    print(outDBName)

# Create Table in employees database
myCursor.execute(
    "CREATE TABLE myDept(DeptID integer, DeptName VARCHAR(30), DeptLoc VARCHAR(20))"
)

# Show tables
myCursor.execute("SHOW TABLES")
myTables = myCursor.fetchall()
for outTable in myTables :
    print(outTable)

# Create table with constraints
myCursor.execute(
    "CREATE TABLE myDept02(DeptID INT(2) NOT NULL AUTO_INCREMENT PRIMARY KEY, DeptName VARCHAR(30), DeptLoc VARCHAR(20))"
)

# Show all columns
myCursor.execute("DESCRIBE myDept02")
deptColumns = myCursor.fetchall()
for columns in deptColumns :
    print(columns)

# Drop Table
myCursor.execute("DROP TABLE myDept")

# Insert data into Table
insertStatement = "INSERT INTO myDept02(DeptName, DeptLoc) VALUES(%s, %s)"
insertValues = [("ACCOUNTING", "NEW YORK"), ("SALES", "BOSTON"), ("TELECOM", "DALLAS"), ("RESEARCH", "CALIFORNIA"), ("OPERATIONS", "ATLANTA")]

myCursor.executemany(insertStatement, insertValues)
db.commit()
print(myCursor.rowcount, "record inserted successfully")

# Show the records
myCursor.execute("SELECT * FROM myDept02")
deptData = myCursor.fetchall()
print("Department data: ", end = "\n")
for data in deptData :
    print(data)

# Filter data
selectStatement = "SELECT * FROM myDept02 ORDER BY DeptID DESC"
myCursor.execute(selectStatement)
fetchRecords = myCursor.fetchall()
print("Department data in descending order: ", end = "\n")
for record in fetchRecords :
    print(record)