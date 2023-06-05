import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 100, 1)
y1 = np.sin(x)
y2 = x ** 2 + 2 * x

plt.figure(4)
ax1 = plt.subplot(221)
ax2 = plt.subplot(222)
ax3 = plt.subplot(223)
ax4 = plt.subplot(224)

ax1.plot(x, y1)
ax2.plot(x, y2)
ax3.plot(x, y1, 'r')
ax4.plot(x, y2, 'r')
plt.tight_layout()

plt.show()

# multiple windows

y1 = np.tan(x)
y2 = x ** 3 + 2 * x
y3 = np.log(x)

plt.figure(1)
ax11 = plt.subplot(211)
ax11.plot(x, y1, 'g')
ax22 = plt.subplot(212)
ax22.plot(x, y2, 'r')

plt.figure(2)
plt.plot(x, y1)

plt.figure(3)
plt.plot(x, y3)

plt.tight_layout()
plt.show()
