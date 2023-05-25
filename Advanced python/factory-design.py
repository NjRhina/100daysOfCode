from abc import ABCMeta, abstractclassmethod

class IPerson(metaclass=ABCMeta):
    @abstractclassmethod
    def person_method():
        """ Interface Method"""

class Student(IPerson):
    def __init__(self):
        self.name = "Basic Student Name"

    def person_method(self):
        print("I am a student")

class Teacher(IPerson):
    def __init__(self):
        self.name = "Basic Teacher Name"

    def person_method(self):
        print("I am a Teacher")

# s1 = Student()
# s1.person_method()

# t1 = Teacher()
# t1.person_method()

class PersonFactory:
    @staticmethod
    def build_person(person_type):
        if person_type == "Student":
            return Student()
        elif person_type == "Teacher":
            return Teacher()
        else:
            print("Invalid type")

if __name__ == "__main__":
    choice = input("what type of person do you want to create? \n")
    person = PersonFactory.build_person(choice)
    person.person_method()
