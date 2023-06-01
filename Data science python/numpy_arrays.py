import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([6, 7, 8, 9, 10])

print(a[0])
print(b[1])

c = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(c)
print(c.shape)

x = np.array([1, 2, 3, 4])
y = np.array([5, 6, 7, 8])
z = x + y

print(z)

# a = np.ones((5,7,3))
# a = np.zeros((5,7,3))
# a = np.full((5, 7, 3), 9)
# a = np.empty((8, 4, 2))
a = np.random.random((5, 5))
print(a)

# x = np.array([0, 5, 10, 15, 20, 25, 30])
x = np.arange(0, 1000, 5)
b = np.linspace(0, 1000, 101)
y = x * 2 - x ** 2
z = np.sin(b)
print(y)
print(z)
print(b)

c = np.array([
    [
        [1, 2, 3],
        [4, 5, 6]
    ],
    [
        [10, 20, 30],
        [40, 50, 60]
    ]
])

print(c.shape)
print(c.size)
print(c.dtype)
