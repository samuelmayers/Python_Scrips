import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0,5,)
y=x**3
#plt.figure(figsize=(15,5))
plt.plot([0,1,2,3,4],[0,1,4,9,16],"go",x,y,"r^")
plt.title('FIRST PLOT')
plt.xlabel('X LABEL')
plt.ylabel('Y LABEL')
plt.show()