import pandas as pd
import mysql.connector as mysql

# SOURCE DATABASE CONNECTION

source_db = mysql.connect(
    host="localhost",
    user="root",
    password="localhost",
    database="source_db"
)

# TARGET DATABASE CONNECTION

target_db = mysql.connect(
    host="localhost",
    user="root",
    password="localhost",
    database="target_db"
)

source_cursor = source_db.cursor()
target_cursor = target_db.cursor()

# READ DATA FROM SOURCE

df = pd.read_sql("SELECT * FROM EMPLOYEE", source_db)

print("Data fetched from source database")
print(df)

# PREPARE DATA FOR UPSERT

data = []

for row in df.itertuples(index=False):

    comm = None if pd.isna(row.COMM) else row.COMM

    data.append((
        row.EMPNO,
        row.ENAME,
        row.JOB,
        row.MGR,
        row.HIREDATE,
        row.HIRETIME,
        row.SAL,
        comm,
        row.DEPTNO
    ))

# UPSERT INTO TARGET DATABASE

target_cursor.executemany("""
    INSERT INTO EMPLOYEE (
        EMPNO, ENAME, JOB, MGR, HIREDATE, HIRETIME, SAL, COMM, DEPTNO
    )
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)

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

target_db.commit()

print(target_cursor.rowcount, "rows inserted/updated in target database")

# CLOSE CONNECTIONS

source_cursor.close()
target_cursor.close()

source_db.close()
target_db.close()