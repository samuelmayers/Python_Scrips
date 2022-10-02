import matplotlib.pyplot as plt
import numpy as np

Div=["Div-A","Div-B","Div-C","Div-D","Div-E"]
valors=[70,82,73,65,68]
valors2=[68,67,77,61,70]

index=np.arange(5)
width=0.30

plt.bar(index,valors,width,color='green',label="Division Marks")
plt.bar(index+width,valors2,width,color='blue',label="Boys Marks")
plt.title("Horizontally Stacked bar Graphs")

plt.xlabel("Division")
plt.ylabel("Marks")
plt.xticks(index+(width/2),Div)

plt.legend(loc='best')
plt.show()
