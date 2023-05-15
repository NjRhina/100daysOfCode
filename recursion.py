n = 7

# finding the factorial in a non recursive way
fact = 1
while n>0:
    fact = fact * n
    n-=1

print(fact)

# finding the factorial in a recursive way
def factorial(n):
    if n<1:
        return 1
    else:
        number = n*factorial(n-1)
        return number

print(factorial(5))

# fibonnaci sequence() without recursion
def fibonnaci(n):
    a,b = 0,1

    for x in range(n ):
        a,b = b, a+b
    return a
print(fibonnaci(100))

# fibonnaci sequence() with recursion
def fibonnaci2(n):
    if n <= 1:
        return n
    else:
        return (fibonnaci2(n-1) + fibonnaci2(n-2))
print(fibonnaci2(100))

