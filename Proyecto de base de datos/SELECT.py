import sqlite3
from sqlite3 import Error
import pandas as pd
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def main():
    database = dir_path+r"\CONNECTION.db"
    conn = create_connection(database)
    with conn:
        df=pd.read_sql_query("SELECT * FROM HOUR",conn)
        print(df)

if __name__ == '__main__':
    main()