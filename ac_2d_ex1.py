import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from atomic_coupling import Universe, Atom

# Number of samples per cluster
n = 100

# Bullseye Clusters
X1 = np.random.multivariate_normal([0,0], [[1,0],[0,1]], n)
X2 = []
for i in np.arange(5*n):
    r = np.random.normal(10, 1, 1)[0]
    theta = np.random.uniform(0, 2*np.pi, 1)[0]
    X2.append([r*np.cos(theta), r*np.sin(theta)])
X2 = np.array(X2)
data = np.concatenate((X1, X2), 0)

# Set dlvo params
params = [1, 1/2, 1/5, 1/3]

# Create universe
ness = Universe(data, params)
ness.draw_universe_2d()

