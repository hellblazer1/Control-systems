import numpy as np
import matplotlib.pyplot as plt
import math

x = np.linspace(0,100,100000)
y1 = (10.01*x) / (1-(0.1*(x**2)))
y2 = (1.1*x) / (1-(0.1*(x**2)))
y = np.arctan(y1) - np.arctan(y2)
plt.title("Phase plot of Transfer function")
plt.plot(x,y)
plt.show()
