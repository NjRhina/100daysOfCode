import numpy as np

a = np.array([
    [1, 2, 3, 10],
    [4, 5, 6, 11],
    [7, 8, 9, 12]
])

b = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 70, 60, 30]
])

# mathematical functions
print(np.sin(a))
print(np.cos(a))
print(np.exp(a))
print(np.sqrt(a))

# aggregate functions
print(a.sum())  # sum of all the numbers in the array
print(a.max())
print(a.min())
print(a.mean())
print(np.median(a))
print(np.std(a))  # standard deviation

# shape manipulating functions
a = a.reshape((4, 3))
print(a)
a = a.reshape((2, 3, 2))
print(a)

a = np.array([
    [1, 2, 3, 10],
    [4, 5, 6, 11],
    [7, 8, 9, 12]
])

print(a.flatten())
print(a.transpose())

for x in a.flat:
    print(x)

print(a.flat[3])

# functions to join arrays
c = np.concatenate((a, b))
print(c)
print('\n')

c2 = np.stack((a, b))
print(c2)
print('\n')

c2 = np.hstack((a, b))  # horizontal stack
print(c2)
print('\n')

c2 = np.vstack((a, b))  # vertical stack
print(c2)

# functions to split an array
print(np.split(a, 3))
print('\n')
print(np.hsplit(a, 2))
print('\n')
print(np.vsplit(a, 3))

# functions for adding values or lists to our array
d = [50, 10, 90, 1]
a = np.append(a, [d], axis=0)
print(a)

a = np.insert(a, 1, d, axis=1)
print(a)
