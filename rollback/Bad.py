import sqlite3

sql=sqlite3.connect(r"C:\Users\samuel mayers\Desktop\Python\rollback\CUENTA.db")
sql.isolation_level=None
c=sql.cursor()
c.execute("begin")
try:
    c.execute("INSERT INTO CUENTA (USUARIO,BALANCE) VALUES('s',5000)")
    c.execute("commit")
except sql.Error:
    print("ERROR!")
    c.execute("rollback")
