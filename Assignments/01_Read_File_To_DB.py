import mysql.connector as mysql
import csv
from datetime import datetime

"""
    Export data from CSV file to Database
        1. Create db connection
        2. Create cursor
        3. Read data from csv file
        4. Create table in database
        5. Insert csv file data into database
        6. Close the connection
"""

# 1. DB connection
db = mysql.connect(
    host = "localhost",
    user = "root",
    password = "localhost",
    database = "source_db"
)

myCursor = db.cursor()

# 2. Read data from csv file
data = []

with open(r"C:\Practice\my-python-journey\DataSets\EmpDataSet.csv", "r") as file :
    csv_reader = csv.reader(file)
    next(csv_reader)

    for row in csv_reader :

        # Convert date format (17-Dec-80 → 1980-12-17)
        hiredate = datetime.strptime(row[4], "%d-%b-%y").strftime("%Y-%m-%d")
        row[4] = hiredate

        # Convert empty COMM to None
        if row[7] == '':
            row[7] = None

        data.append(tuple(row))

# 3. Create table in database
myCursor.execute("""
    CREATE TABLE EMPLOYEE
        (EMPNO INT NOT NULL PRIMARY KEY,
        ENAME VARCHAR(30),
        JOB VARCHAR(20),
        MGR VARCHAR(10),
        HIREDATE DATE,
        HIRETIME TIME,
        SAL INT,
        COMM INT,
        DEPTNO INT
    )
    """)

print("Employee table is created")

# 4. Insert data into table from csv file
myCursor.executemany("""
    INSERT INTO EMPLOYEE(
        EMPNO,
        ENAME,
        JOB,
        MGR,
        HIREDATE,
        HIRETIME,
        SAL,
        COMM,
        DEPTNO
        ) VALUES (
            %s, %s, %s, %s, %s, %s, %s, %s, %s
            )
        """, data)
db.commit()

print(myCursor.rowcount, "Rows are inserted")

myCursor.close()