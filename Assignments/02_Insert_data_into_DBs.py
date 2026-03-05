import mysql.connector as mysql

"""
    Transfer data from one Database table to another database
        1. Create source and target db connections
        2. Create cursors
        3. Create table in Target_db
        4. Fetch data from source_Db
        5. Insert data into target_db
        6. Close the connections
"""

# Source DB connection
source_db = mysql.connect(
    host = "localhost",
    user = "root",
    password = "localhost",
    database = "source_db"
)

# Target DB connection
target_db = mysql.connect(
    host = "localhost",
    user = "root",
    password = "localhost",
    database = "target_db"
)

# define cursors
source_cursor = source_db.cursor()
target_cursor = target_db.cursor()

# 3. Create table in target db
target_cursor.execute("""
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

print("Employee table is created in target db")

# Fetch data from souce_db
source_cursor.execute("SELECT * FROM EMPLOYEE")
rows = source_cursor.fetchall()

# Insert data into target_db
target_cursor.executemany("""
                          INSERT INTO employee(
                                EMPNO,
                                ENAME,
                                JOB,
                                MGR,
                                HIREDATE,
                                HIRETIME,
                                SAL,
                                COMM,
                                DEPTNO
                            )
                            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
                        """, rows)

target_db.commit()
print(target_cursor.rowcount, "rows transferred")

source_cursor.close()
target_cursor.close()