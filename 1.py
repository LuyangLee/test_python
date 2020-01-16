import matplotlib.pyplot as plt
import numpy as np 
x = np.linspace(0,6,300)
x1 = np.array([[0,0],[0,2],[2,0],[2,2]])
x2 = np.array([[4,4],[4,6],[6,4],[6,6]])

plt.plot(x, 6 - x, label = 'linear')
plt.scatter([i[0] for i in x1],[i[1] for i in x1], marker='v', s=30, alpha=0.5)
plt.scatter([i[0] for i in x2],[i[1] for i in x2], marker='v', s=30, alpha=0.5)
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()