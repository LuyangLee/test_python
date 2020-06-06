import numpy as np 
import matplotlib.pyplot as plt
from sklearn import manifold
from mpl_toolkits.mplot3d import Axes3D
from functools import reduce
import operator

N = 1000
neighbors = 12
components = 2
noise = 0.001*np.random.randn(1, N)
tt = (3*np.pi/2)*(1+2*np.random.rand(1,N))
height = 21*np.random.rand(1,N)
X = np.concatenate(((tt + noise)*np.cos(tt), height, (tt + noise)*np.sin(tt)), axis=0).T
color = tt.reshape(-1)

## Isomap
Y1 = manifold.Isomap(n_neighbors=neighbors, n_components=components).fit_transform(X)
print(Y1.shape)

## LLE
Y2 = manifold.LocallyLinearEmbedding(n_neighbors = neighbors,n_components= components, method='standard').fit_transform(X)

## LE
Y3 = manifold.SpectralEmbedding(n_components= components,n_neighbors= neighbors).fit_transform(X)

## draw
fig = plt.figure()
ax1 = fig.add_subplot(221,projection='3d')
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)
ax1.scatter(X[:,0],X[:,1],X[:,2],s = 5, c=color, cmap='Spectral_r')
ax1.set_title("SwissRoll")
ax2.scatter(Y1[:,0],Y1[:,1],s = 5,c=color, cmap='Spectral_r')
ax2.set_title("Isomap")
ax3.scatter(Y2[:,0],Y2[:,1],s = 5,c=color, cmap='Spectral_r')
ax3.set_title("LLE")
ax4.scatter(Y3[:,0],Y3[:,1],s = 5,c=color, cmap='Spectral_r')
ax4.set_title("LE")
plt.show()