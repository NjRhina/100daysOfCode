import numpy as np
import matplotlib.pyplot as plt

mu, sigma = 173, 8
x = mu + sigma * np.random.randn(10000)

plt.title("Normal distribution curve of heights of students")
plt.xlabel('Heights')
plt.ylabel('Percentage of students')
plt.text(140, 0.4, "mu=173, sig=8")

plt.hist(x, 100, facecolor='blue', density=True)
plt.show()
