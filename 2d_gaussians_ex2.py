import numpy as np
import matplotlib.pyplot as plt

n = 500 # number of samples per cluster

X1 = np.random.multivariate_normal([0,0], [[1,0],[0,1]], n)

X2 = []
for i in np.arange(5*n):
    r = np.random.normal(10, 1, 1)[0]
    theta = np.random.uniform(0, 2*np.pi, 1)[0]
    X2.append([r*np.cos(theta), r*np.sin(theta)])
X2 = np.array(X2)

plt.plot(X1[:,0], X1[:,1], 'r.')
plt.plot(X2[:,0], X2[:,1], 'b.')
plt.show()