from sqlalchemy import create_engine

import os
dir_path = os.path.dirname(os.path.realpath(__file__))
engine = create_engine(r'sqlite:///'+dir_path+'\student.db', echo=True)

