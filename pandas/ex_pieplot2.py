from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
import pandas as pd
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
file=dir_path+r'\Northwind.xls'

df=pd.read_excel(file,'Customers')
colors=['red','green','blue','silver','gold','white','gray','lightblue','yellow','brown']
df['Country'].value_counts().plot(kind='pie',colors=colors,title='Country By Customers')
plt.axis('equal')
plt.show()