import queue

################## first in first out queue ###################
q1 = queue.Queue()

numbers = [10, 20, 30, 40, 50, 60, 70]
for number in numbers:
    q1.put(number)

print(q1.get())


################## last in first out queue ###################
q2 = queue.LifoQueue()

numbers = [10, 20, 30, 40, 50, 60, 70]
for number in numbers:
    q2.put(number)

print(q2.get())


################## customize what is first out queue ###################
q3 = queue.PriorityQueue()

#hello word has a priority of one
q3.put((1, "Hello, World"))
q3.put((2,10))
q3.put((5,7.5))
q3.put((3,True))

while not q3.empty():
    print(q3.get()[1])
    print(q3.get()[1])
    print(q3.get()[1])
    print(q3.get()[1])

