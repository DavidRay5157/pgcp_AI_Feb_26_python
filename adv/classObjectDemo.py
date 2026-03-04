'''
class Computer:
    #def __init__(self):    # self is reffering to the current instance of the class
    #    print("in computer")

    #def __init__(self, name, price):   # here method overloading is not supported
     #   self.name = name
     #   self.price = price

    def __init__(self, name, price, gpu):
        self.name = name      # this are the attributes of the class
        self.price = price
        self.gpu = gpu

    def config(self):     # this is the behaviour
        print("this is the configuration of the computer ", self.name)




com1 = Computer("asus", 2000, "RTX")
print(type(com1))
com1.config()

Computer.config(com1)



class Computer:
    def __init__(self):
        self.name = "acer"
        self.price = 200

    def update(self):
        self.price = 100

    def compare(self, other):
        if self.price == other.price:
            return True
        else:
            return False

com1 = Computer()
print(com1.price)
com1.update()
print(com1.price)

com2 = Computer()
print(com2.price)

if com1.compare(com2):
    print("same")
else:
    print("not same")
'''


class Student:
    # class variable (shared to all the students)
    school = "ABC school"

    def __init__(self, name, marks):
        # instance variables (unique for each object)
        self.name = name
        self.marks = marks


# creating object
s1 = Student("John", 100)
s2 = Student("david", 500)

print(s1.name, s1.marks)
print(s2.name, s2.marks)

print(s1.school)
print(s2.school)

# change class variable
Student.school = "KBC school"
print(s1.school)

s2.school = "XYZ"  # this is uniquly changing the value of school
print(s1.school)
print(s2.school)

print("this is student school printing")
print(Student.school)



