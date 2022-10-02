import timeit

code_to_test1 = """
import matplotlib.pyplot as plt
import numpy as np

x=np.arange(1,6)
y=x**3
#plt.figure(figsize=(15,5))
plt.plot([0,1,2,3,4],[0,1,4,9,16],"go")
plt.title("1st subplot")

#plt.show()
"""
code_to_test2 = """
import matplotlib.pyplot as plt

Div=["Div-A","Div-B","Div-C","Div-D","Div-E"]
valors=[70,82,73,65,68]

plt.bar(Div,valors,color='black')
plt.title("Bar Graph")
plt.xlabel("Division")
plt.ylabel("Marks")
#plt.show()

"""
speed1 = timeit.timeit(code_to_test1, number=100)
speed2 = timeit.timeit(code_to_test2, number=100)
print(speed1)
print(speed2)
