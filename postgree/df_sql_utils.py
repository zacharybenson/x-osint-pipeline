''' twitter_api_utils.py
* ====================================================================================
* Name: Zachary Benson, Jan 2022
* Project: OSINT Pipeline
* Purpose: This file contains the neccessary utilities to pass df to postgree.
* Contact Information: 
*     Email: zachary.n.benson@gmail.com
* ===================================================================================== 
'''
import psycopg2
import psycopg2.extras as extras
import pandas as pd
import sqlalchemy
from urllib.parse import quote

#Connection to the database
conn = psycopg2.connect(
   database="postgres",
    user='zacharybenson',
    password='1qaz@WSX3edc',
    host='localhost',
    port= '5432'
)

def execute_values(df):
    df = df[['id','created_at','text']]
         # Create the engine to connect to the PostgreSQL database
    engine = sqlalchemy.create_engine('postgresql://zacharybenson:%s@localhost:5432/postgres' % quote('1qaz@WSX3edc'))
    
    df.to_sql('tweets',engine,if_exists='append')

def create_db(conn):
    #establishing the connection
    conn.autocommit = True

    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    #Preparing query to create a database
    sqlDB = '''CREATE database ''';

    #Creating a database
    try:
        cursor.execute(sqlDB)
        print("Database created successfully.")
    except Exception as e: print(e)
    cursor.close()

def create_table():
    conn.autocommit = True

    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    #Creating a table
    sqlT = '''CREATE TABLE tweet (
        Tweet_ID VARCHAR(20),
        Tweet_Date DATE,
        Tweet_Text VARCHAR(280),
        PRIMARY KEY (Tweet_ID)
        )'''

    #Creating a database
    try:
        cursor.execute(sqlT)
        print("Table created successfully.")
    except Exception as e: print(e)
    cursor.close()

def main(df):
    execute_values(df)
