'''
class Computer:
    #def __init__(self):   # default constructor
     #   print("constructor")

    #def __init__(self, name, price):   # constuctor overloading is not supported
    #    self.name = name
    #    self.price = price

    def __init__(self, name, price, gpu):
        self.name = name
        self.price = price
        self.gpu = gpu

    def config(self):
        print("config", self.name, self.price, self.gpu)

c1 = Computer("HP", 2000, "gtx")
c1.config()
print(c1.gpu)
print(type(c1))

Computer.config(c1)

class Computer:

    def __init__(self):   # constuctor overloading is not supported
        self.name = "ACER"
        self.price = 2000

    def update(self):
        self.price = 8000

    def compare(self, other):
        if self.price == other.price:
            return True
        else:
            return False

com1 = Computer()
com2 = Computer()

print(com1.price)
com1.update()
print(com1.price)
print(com2.price)

if com1.compare(com2):
    print("same")
else:
    print("not same")
    '''

class Student:
    school = "ABC school"   # class variable (shared to all the objects )
    def __init__(self, name, rollno):
        self.name = name   # this are instance variables (unique for each objects)
        self.rollno = rollno

s1 = Student("david", 1)
s2 = Student("harsvardhan PATEL", 100)

print(s1.name, s1.rollno)
print(s2.name, s2.rollno)

print(s1.school)
print(s2.school)

Student.school = "KBC school"
print(s1.school)
print(s2.school)

s2.school = "XYZ"
print("after xyz school")
print(s1.school)
print(s2.school)

print("final printing")
print(Student.school)

























