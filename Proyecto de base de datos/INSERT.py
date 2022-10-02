import sqlite3
from sqlite3 import Error
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def create_project(conn, Employee):
   sql = """INSERT INTO EMPLOYEE(end_date)
            VALUES(?)"""
   cur = conn.cursor()
   cur.execute(sql, Employee)
   return cur.lastrowid

def Introduce_Hours(conn, Hour):
    sql = """ INSERT INTO HOUR (EMPLOYEE,SUPORT_HOUR,DEV_HOUR,TRAINING_HOUR)
              VALUES(?,?,?,?) """
    cur = conn.cursor()
    cur.execute(sql,Hour)
    return cur.lastrowid

def main():
    database = dir_path+r"\CONNECTION.db"
    # create a database connection
    conn = create_connection(database)
    with conn:
        # create a new Employee
        #Employee = ('', '', '')
        #create_project(conn, Employee)
        Hour=[0,0,0,0]
        Hour[0]=int(input('introduce el ID del empleado '))
        Hour[1]=int(input('introduce las horas de soporte '))
        Hour[2]=int(input('introduce las horas de desarrollo '))
        Hour[3]=int(input('introduce las horas de entrenamiento '))
        #Hour=(Hour1,Hour2,Hour3,Hour4)
        Introduce_Hours(conn, Hour)

if __name__ == '__main__':
    main()
