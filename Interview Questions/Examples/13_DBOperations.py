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
    "CREATE TABLE myDept01(DeptID INT(2) NOT NULL AUTO_INCREMENT PRIMARY KEY, DeptName VARCHAR(30), DeptLoc VARCHAR(20))"
)

# Insert data into Table
insertStatement = "INSERT INTO myDept01(DeptName, DeptLoc) VALUES(%s, %s)"
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

# Copy all myDept01 table records into mydept table
myCursor.execute("""
    INSERT INTO myDept(DeptName, DeptLoc)
    SELECT DeptName, DeptLoc FROM myDept01
""")
db.commit()
print("Data copied successfully")
