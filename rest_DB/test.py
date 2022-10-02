from flask import Flask, render_template, request, redirect, url_for 
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

app = Flask(__name__)

@app.route('/')
def index():
      return render_template('index.html')

def Introduce_User(conn, User):
    sql = """ INSERT INTO USER (Nombre,Apellido) VALUES(?,?) """
    cur = conn.cursor()
    cur.execute(sql,User)
    return cur.lastrowid
@app.route('/user',methods=['POST'])
def user():

  if request.method == 'POST':
    database = dir_path+r"\user.db"
    # create a database connection
    conn = create_connection(database)
    with conn:
      Nombre=str(request.form['Nombre'])
      Apellido=str(request.form['Apellido'])
      User=[Nombre,Apellido]
      Introduce_User(conn,User)
      return "Succed"

if __name__ == '__main__':
    app.run(host='127.0.0.1',debug=True)