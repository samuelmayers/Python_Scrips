import sqlite3
from sqlite3 import Error
import pandas
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    try:
        cur = conn.cursor()
        cur.execute(create_table_sql)
    except Error as e:
        print(e)

def main():
    database = dir_path+r"\CONNECTION.db"

    table_employee = """CREATE TABLE "EMPLOYEE" (
	"EMPLOYEE_ID"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"NAME"	TEXT NOT NULL
    ); """

    table_hours = """CREATE TABLE "HOUR" (
	"HOUR_ID"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"EMPLOYEE"	INTEGER NOT NULL,
	"SUPPORT_HOUR"	INTEGER NOT NULL,
	"DEV_HOUR"	INTEGER NOT NULL,
	"TRAINING_HOUR"	INTEGER,
	FOREIGN KEY("EMPLOYEE") REFERENCES "EMPLOYEE"("EMPLOYEE_ID")
    );"""

    conn = create_connection(database)

    if conn is not None:
        create_table(conn, table_employee)
        create_table(conn, table_hours)
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()