import matplotlib.pyplot as plt
import numpy as np

Div=["Div-A","Div-B","Div-C","Div-D","Div-E"]
valors2=[68,67,77,61,70]
valors3=[72,97,69,69,66]

index=np.arange(5)
width=0.30

plt.bar(index,valors2,width,color='blue',label="Boys Marks")
plt.bar(index,valors3,width,color='red',label="Girls Marks",bottom=valors2 )
plt.title("Horizontally Stacked bar Graphs")

plt.xlabel("Division")
plt.ylabel("Marks")
plt.xticks(index,Div)

plt.legend(loc='best')
plt.show()
