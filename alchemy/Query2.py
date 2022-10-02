import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from prueba import *

engine = create_engine(r'sqlite:///'+dir_path+'\student.db', echo=True)

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

# Create objects  
for student in session.query(Student).filter(Student.firstname == 'Eric'):
    print(student.firstname, student.lastname)