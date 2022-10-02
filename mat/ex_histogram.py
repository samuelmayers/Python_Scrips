import matplotlib.pyplot as plt
import numpy as np


x=np.random.randn(1000)

plt.title("Histogram")
plt.xlabel("Ramdom Data")
plt.ylabel("Frequency")
plt.hist(x,10)
print(x)
plt.show()
