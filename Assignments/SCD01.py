import mysql.connector as mysql
import pandas as pd

# 1. DB connection
db = mysql.connect(
    host = "localhost",
    user = "root",
    password = "localhost",
    database = "source_db"
)

myCursor = db.cursor()

# Source Table

myCursor.execute("""
                 CREATE TABLE IF NOT EXISTS source_employee (
                 emp_id INT PRIMARY KEY,
                 emp_name VARCHAR(50),
                 salary INT,
                 updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
                )
                """)

print("Source table is created")

# Target Table
myCursor.execute("""
                 CREATE TABLE IF NOT EXISTS target_employee (
                 emp_id INT PRIMARY KEY,
                 emp_name VARCHAR(50),
                 salary INT,
                 updated_at TIMESTAMP
                 )
                 """)

print("Target table is created")

# Insert initial data into Source
myCursor.execute(
    """INSERT IGNORE INTO source_employee (emp_id, emp_name, salary) VALUES
        (1, 'John', 5000),
        (2, 'Alice', 6000),
        (3, 'Bob', 5500)
    """)
print(myCursor.rowcount, "Rows inserted")

# Fetch data from souce_table
myCursor.execute("SELECT * FROM source_employee")
rows = myCursor.fetchall()

# Insert data into target_db
myCursor.executemany("""
                        INSERT IGNORE INTO target_employee(
                        emp_id,
                        emp_name,
                        salary,
                        updated_at
                        )
                            VALUES (%s,%s,%s, %s)
                        """, rows)

db.commit()
print(myCursor.rowcount, "rows transferred")

# Step 1: Get last updated timestamp from target
myCursor.execute("SELECT MAX(updated_at) FROM target_employee")
last_updated = myCursor.fetchone()[0]

if last_updated is None:
    last_updated = "1900-01-01"

print("Last Updated Timestamp:", last_updated)

# Step 2: Read only new/updated records from source
query = f"""
SELECT * FROM source_employee
WHERE updated_at >= '{last_updated}'
"""

df = pd.read_sql(query, db)
print("New/Updated Records:")
print(df)

# Step 3: Insert/Update into target table
for index, row in df.iterrows():
    myCursor.execute("""
    INSERT INTO target_employee (emp_id, emp_name, salary, updated_at)
    VALUES (%s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE
        emp_name = VALUES(emp_name),
        salary = VALUES(salary),
        updated_at = VALUES(updated_at)
    """, (
        row.emp_id,
        row.emp_name,
        row.salary,
        row.updated_at
    ))

db.commit()

print("Incremental Load Completed!")

myCursor.close()
db.close()
