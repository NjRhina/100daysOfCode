import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

plt.figure(1)
ax1 = plt.axes(projection="3d")

z = np.linspace(0, 30, 100)
x = np.sin(z)
y = np.cos(z)

ax1.plot3D(x, y, z)
plt.show()

plt.figure(2)

ax2 = plt.axes(projection="3d")


def c_function(a, b):
    return np.sin(np.sqrt(a ** 2 + b ** 2))


a = np.linspace(-5, 5, 100)
b = np.linspace(-5, 5, 100)

A, B = np.meshgrid(a, b)
C = c_function(A, B)

ax2.plot_surface(A, B, C)

plt.show()
