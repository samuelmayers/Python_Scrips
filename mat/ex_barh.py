import matplotlib.pyplot as plt

Div=["Div-A","Div-B","Div-C","Div-D","Div-E"]
Div_Marks=[70,82,73,65,68]
variance=[5,8,7,6,4]

plt.barh(Div,Div_Marks,xerr=variance,color='red')
plt.title("Bar Graph")
plt.xlabel("Division")
plt.ylabel("Marks")
plt.show()