class Person:

    #this is a constructor
    def __init__(self,name, age):
        self.name = name
        self.age = age

    # this is string method
    def __str__(self):
        return "Name: {}, Age: {}".format(self.name, self.age)

class Worker(Person):

    def __init__(self, name, age, salary ):
        super(Worker,self).__init__(name,age)
        self.salary = salary

    def calc_yearly_salary(self):
        return self.salary * 12

    def __str__(self):
        text = super(Worker, self).__str__()
        text += ", Salary: {}".format(self.salary)
        return text


Worker1 = Worker("Nana", 20, 500000)

print(Worker1.calc_yearly_salary())

print(Worker1)



# example 2 (operator overloading)

class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self,other):
        return Vector (self.x + other.x, self.y + other.y)

    def __sub__(self,other):
        return Vector (self.x - other.x, self.y - other.y)

    def __str__(self):
        return ("x({}), y({})".format(self.x, self.y))

v1 = Vector(2,7)
v2 = Vector(5,3)

print(v1)
print(v2)

v3 = v1 - v2
v4 = v1 + v2

print(v3)
print(v4)

