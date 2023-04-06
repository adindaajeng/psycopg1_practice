#!pip install psycopg2-binary
#!pip install python-dotenv

# Import library
import psycopg2
import os
from dotenv import load_dotenv, find_dotenv

# Connect to Postgre
"""
Create a new database session and return a new connection object. The basic connection parameters are:

dbname – the database name (database is a deprecated alias)
user – user name used to authenticate
password – password used to authenticate
host – database host address (defaults to UNIX socket if not provided)
port – connection port number (defaults to 5432 if not provided)
"""

# Load .Env
load_dotenv(find_dotenv())

conn = psycopg2.connect(
    dbname = os.getenv("DATABASE_NAME"),
    user = os.getenv("DATABASE_USERNAME"),
    password = os.getenv("DATABASE_PASSWORD"),
    host = os.getenv("DATABASE_HOST"),
    port = os.getenv("DATABASE_PORT")
)

# Create Cursor
"""
Allows Python code to execute PostgreSQL command in a database session. Cursors are created by the connection.cursor() method: they are bound to the connection for the entire lifetime and all the commands are executed in the context of the database session wrapped by the connection. Cursor Method are:

execute
    DML, dan DDL yang outputnya cuma 1
executemany
    DML, dan DDL yang outputnya cuma tergantung n
fetchone
    read data dan menampilkan 1 hasil
fetchmany
    read data dan menampilkan n hasil
fetchall
    read data dan menampilkan semua hasil
"""
cur = conn.cursor()

# Create table on selected database
cur.execute(
    ''' 
    CREATE TABLE regions(
        region_id SERIAL PRIMARY KEY,
        region_name VARCHAR(50) NOT NULL
    );
    '''
)

conn.commit()

# Insert data
cur.execute(
    '''
    INSERT INTO regions(region_id, region_name)
    VALUES (
        1, 'Australia'
    )
    '''
)
conn.commit()

# Close Connection
cur.close()
conn.close()