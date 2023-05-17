class Person:

    number_of_people = 0

    #this is a constructor
    def __init__(self,name, age):
        self.name = name
        self.age = age
        Person.number_of_people +=1

    # this is a destructor
    def __del__(self):
        print ("Object deleted")
        Person.number_of_people -=1

    # this is string method
    def __str__(self):
        return "Name: {}, Age: {}".format(self.name, self.age)

x = Person("Rhina", 24)
print (x.name, x.age)

y = Person("Rhina", 24)
print (y.name, y.age)

z = Person("Rhina", 24)
print (z.name, z.age)

print(x)
print(y)
print(z)
print (Person.number_of_people)

del x

print (Person.number_of_people)


