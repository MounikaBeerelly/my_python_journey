import mysql.connector as mysql
import os

os.system("cls")

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "localhost",
    database = "studenttable"
)

myCursor = db.cursor()

# Create 2 Tables in studenttable database
myCursor.execute(
    "CREATE TABLE source_student(StudentID INT(3) NOT NULL AUTO_INCREMENT PRIMARY KEY, StudentName VARCHAR(30), StudentAge int(2))"
)

myCursor.execute(
    "CREATE TABLE target_student(StudentID INT(3) NOT NULL AUTO_INCREMENT PRIMARY KEY, StudentName VARCHAR(30), StudentAge int(2))"
)

# Insert data into Table
insertStatement = "INSERT INTO source_student(StudentName, StudentAge) VALUES(%s, %s)"
insertValues = [("John", 26), ("Smith", 21), ("Scott", 35), ("Jones", 19), ("David", 27)]

myCursor.executemany(insertStatement, insertValues)
db.commit()
print(myCursor.rowcount, "records inserted successfully")


# Copy all source_student table records into target_student table

# Step 1: Fetch data from source table
myCursor.execute("SELECT StudentName, StudentAge FROM source_student")
rows = myCursor.fetchall()

# Step 2 : Insert data into target table
insertStatement = "INSERT INTO target_student (StudentName, StudentAge) VALUES (%s, %s)"
myCursor.executemany(insertStatement, rows)

db.commit()
print("Data copied successfully")
