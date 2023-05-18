class Persons:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print("The object is being deconstructed")

p = Persons("NANA",23)


class Vector:
    def __init__(self, x, y): #magic method/dundler
        self.x = x
        self.y = y

    def __add__(self,other): #magic method/dundler
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self): #magic method/dundler
        return f"X:{self.x},Y:{self.y}"

v1 = Vector(28, 30)
v2 = Vector(10, 24)
v3 = v1+v2

print(v3)
print(v3.x)
print(v3.y)
