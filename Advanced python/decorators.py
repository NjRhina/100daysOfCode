import time

def mydecorator(function):

    def wrapper(*args, **kwargs):
        function(*args, **kwargs)
        print("I am decorating your function!")
    return wrapper

@mydecorator
def hello(person):
    print(f"Hello {person}!")

hello("Namono")

# practical example #1

def logged(function):
    def wraper(*args, **kwargs):
        value = function(*args, **kwargs)
        with open('logfile.txt','a+') as f:
            fname = function.__name__
            print(f"{fname} returned value {value}")
            f.write(f"{fname} returned value {value}\n")
        return value
    return wraper


@logged
def add(x,y):
    return x+y

print(add(10,20))


# practical example #2
def timed(function):
    def wrapp(*args, **kwargs):
        before = time.time()
        value = function(*args, **kwargs)
        after = time.time()
        fname = function.__name__
        print(f"{fname} took {after-before} seconds to execute")
        return value
    return wrapp

@timed
def myfunction(x):
    result = 1
    for i in range(1,x):
        result*=i
    return result

myfunction(1000)
