import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

from atomic_clustering import Universe, Atom

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
params = [1, 10, 1/50, 10]

# Create universe
ness = Universe(data, params)
fr = []
num = 50
for i in np.arange(num):
    print(i)
    ness.attraction()
    fr.append(ness.return_frame())

#ness.draw_universe_2d()

# animation function.  This is called sequentially
def animate_1D(i, *X):
    dat = X[i]
    bullseye.set_data(dat[0], dat[1])
    return bullseye,

fig = plt.figure()
ax = plt.axes(xlim=(-15, 15), ylim=(-15, 15))
bullseye, = ax.plot([], [], 'r.')

anim = animation.FuncAnimation(fig, animate_1D, fargs=fr, frames=len(fr), interval=100, blit=True)

'''
plt.rcParams['animation.ffmpeg_path'] = './ffmpeg'
mywriter = animation.FFMpegWriter(fps=60)
anim.save('burgers_equation_1D.mp4', writer=mywriter)
'''

plt.show()