#import describe_object


# This is object of class
# There is only one object of the same class.

class Student:
    def __init__(self, name= 'Anton'):
        self.name= name
        print(self.name)
        print(name)
        name = 'den'
        print(self)


from utils import describe_object


class Student:
    def __init__(self, name):
        pass

print(describe_object(name="Student", obj=Student))
# This is instances of class Student

# It could be a lot of instances of one class

student_1 = Student('Oly')
student_2 = Student('Denys')
print(student_2.name)

student_1 = Student()

student_2 = Student()


student_3 = Student()

print(describe_object("student_1", student_1))
print(describe_object("student_2", student_2))
print(describe_object("student_3", student_3))



class Programer:

    def __init__(self, name, language = "Python", position = "junior") -> None:
        self.name = name
        self.language = language
        self.position = position
        self.enough_coffee = False
    print('Initialization')

    def __new__(cls, *args, **kwargs):
        obj = super(Programer, cls).__new__(cls)
        return obj
    print("New")


    def __str__(self):
        print(str(Programer))


    def __repr__(self):
        def some_func():
            return


some_int = 10

