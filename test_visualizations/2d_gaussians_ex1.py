import numpy as np
import matplotlib.pyplot as plt

n = 1000 # number of samples per cluster

X1 = np.random.multivariate_normal([0,0], [[1,0],[0,1]], n)             # Cluster 1
X2 = np.random.multivariate_normal([0,5], [[1,0.25],[0.25,1]], n)       # Cluster 2
X3 = np.random.multivariate_normal([5,2.5], [[1,0.5],[0.5,1]], n)       # Cluster 3

plt.plot(X1[:,0], X1[:,1], 'r.')
plt.plot(X2[:,0], X2[:,1], 'b.')
plt.plot(X3[:,0], X3[:,1], 'g.')
plt.show()