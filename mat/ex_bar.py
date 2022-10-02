import matplotlib.pyplot as plt

Div=["Div-A","Div-B","Div-C","Div-D","Div-E"]
valors=[70,82,73,65,68]

plt.bar(Div,valors,color='black')
plt.title("Bar Graph")
plt.xlabel("Division")
plt.ylabel("Marks")
plt.show()
