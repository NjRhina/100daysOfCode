#Seq 1 to 9,000,000

def mygenerator(n):
    for x in range(n):
        yield x**3

values = mygenerator(9000000)

print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))

def infinite_sequence():
    result = 1
    while True:
        yield result
        result*=5

value = infinite_sequence()

for x in range(500, 700):
    print(next(value))

