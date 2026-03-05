import pandas as pd
import mysql.connector as mysql
from datetime import datetime

# 1. DB connection
db = mysql.connect(
    host = "localhost",
    user = "root",
    password = "localhost",
    database = "source_db"
)

myCursor = db.cursor()

# read data from db and store as dataframe
df= pd.read_sql("SELECT * FROM EMPLOYEE", db)

print("Fetching data from database : ", end = "\n")
print(df)

# Insert new row into dataframe
new_row = {
    "EMPNO": 7744,
    "ENAME": "JOCKY",
    "JOB": "CLERK",
    "MGR": 7698,
    "HIREDATE": "1981-12-06",
    "HIRETIME": "02:30:04",
    "SAL": 1950,
    "COMM": None,
    "DEPTNO": 20
}

df.loc[len(df)] = new_row
print("New row is inserted. Total number of rows are: ", len(df))

df = df.drop_duplicates(subset="EMPNO")

# update existing row in dataframe
df.loc[df["EMPNO"] == 7369, "SAL"] = 3000
print("EMPNO 7369 is updated.")

# Prepare data for insert/update
data = []
for row in df.itertuples(index = False) :
    # convert null values to None
    comm = None if pd.isna(row.COMM) else row.COMM
    # convert date format
    hiredate = row.HIREDATE
    data.append((row.EMPNO, row.ENAME, row.JOB, row.MGR, hiredate, row.HIRETIME, row.SAL, comm, row.DEPTNO))

# Insert/Update into database UPSERT
myCursor.executemany("""
                     INSERT INTO EMPLOYEE (
                         EMPNO, ENAME, JOB, MGR, HIREDATE, HIRETIME, SAL, COMM, DEPTNO
                     ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                     ON DUPLICATE KEY UPDATE
                     ENAME = VALUES(ENAME),
                     JOB = VALUES(JOB),
                     MGR = VALUES(MGR),
                     HIREDATE = VALUES(HIREDATE),
                     HIRETIME = VALUES(HIRETIME),
                     SAL = VALUES(SAL),
                     COMM = VALUES(COMM),
                     DEPTNO = VALUES(DEPTNO)
                """, data)

print(myCursor.rowcount, "rows inserted/updated successfully")

# Sort Dataframe by SAL column
df = df.sort_values(by = "SAL", ascending = False)
print("Data after sorting :", df)

db.commit()

myCursor.close()
db.close()