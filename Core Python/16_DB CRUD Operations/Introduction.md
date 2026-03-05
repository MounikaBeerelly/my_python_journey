### What is the Pre-Requisite to connect Python with a Database ?
1. Python as a languauge, should provide a database connectivity API, OR the database vendor should provide the API.
2. Python provides standard database connectivity interface called as `DB-API of Python`.
3. The `Python DB-API` can be connected to any database that adjers to the stsndard that is expected by Python.
4. To connect with `Python DB-API` we need the support of `ODBC (Operating DataBase Connecctivity)` from the Operating system.

### What we need if we want to connect to Databases using Python?
1. Download the `DB-API module` for each database that we need to connect, cross checking the proper version of the Python that is supported.
    - `https://wiki.python.org/moin/MySQL`
2. The DB-API will provide minimal standards for working with databases, by using Python structures.

### What steps we need to operate with DB-API ?
1. Import the API module
2. Setup OR aquire the Database connection
3. Issue OR execute the SQL statements and stored procedures if available
4. Close the connection once all the required operations on the database are done

### Setup Database using Python
1. Installing the required database on the machine.
2. Installing OR Configuring the database connector for Python

### Requirements to design and develop one software application:
1. Data Storage Architecture
    1. Primary Memory Based (RAM, variables)
    2. Auxilary OR Physical Storage
        1. File Based
            1. Developer should develop all the routines for
                1. Creating the structures
                2. Write all the required CRUD operations
        2. Database Oriented
            1. Learn and use SQL effectively
2. Business Operational Architecture
    1. Using any Programming Language having Procedural Logic Features
    2. The Language should have the ability to establish connectivity to database
        1. ODBC
        2. JDBC
        3. DSN with CGI
        4. Language Specific Database Connectors
3. Data presentation OR Visualization Architecture
    1. Form Based (Business Operations OR Transactions Based)
        1. CLI (Command Line Interface)
        2. GUI (Graphical User Interface)
            1. Windows Based (Stand alone GUI's)
            2. Web Based (Browser Based)
                1. Macro Browser
                2. Micro Browser
    2. Reports Based (Business Data Presentation)
        1. Text Based
        2. Graph Based

### Requirements to design and develop one Software Database application :
- **STEP 1 - Database Selection**
    1. Database Installation and Configuration (DBA)
        - https://downloads.mysql.com/archives/installer/
- **STEP 2 - Middle Layer Software Selection**
    1. Operational Software Installation and Configuration with specific database connector

#### Ensuring PIP in the Machine :
- python -m ensurepip

#### Installing PIP on the machine :
- python -m pip install -U

#### Upgrading PIP package :
- python -m pip install -- upgrade pip setuptools

#### Installing MySQL Connector :
- pip install -U mysql-connector-python --user

#### Check the MySQL installation
- Open command prompt -> go to python shell and type below commands
```
import mysql.connector as mysql
db = mysql.connect (
    host = "localhost",
    user = "root",
    passwd = "localhost"
)
print(db)
```
- We use db.cursor() because a database connection alone cannot execute SQL queries. The cursor is the object that actually executes SQL statements, fetches results, and manages query state.
```
    myCursor = db.cursor()
```