import threading

def function1():
    for x in range (100):
        print("ONE")

def function2():
    for x in range (150):
        print("TWO")

def hello():
    for x in range (50):
        print("Hello")

t1 = threading.Thread(target=function1)
t2 = threading.Thread(target=function2)
t3 = threading.Thread(target = hello)

t1.start()
t2.start()
t3.start()

t1.join()

print("Good day")
