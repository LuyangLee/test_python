import matplotlib.pyplot as plt 
import numpy as np 

t = np.linspace(-np.pi,0) + (np.linspace(0., np.pi))
print(type(t))
X = 2*(np.cos(t) - np.cos(2*t))
Y = 2*(np.sin(t) - np.sin(2*t))
plt.plot(Y, X)
plt.show()