# class variables = shared among all the objects.
# instance varibales = for objects, unique for objects.

class Student:

    school = 'cdac'   # class variable

    def __init__(self, m1, m2 ,m3):
        self.m1 = m1      # instance variable
        self.m2 = m2
        self.m3 = m3

    def avg(self):   # instance method, because we pass self.
        return (self.m1 + self.m2 + self.m3) / 3

    def get_m1(self):   # getter method, in python we call accessor
        return self.m1

    def set_m1(self, value):   # setter method, we call in python mutators
        self.m1 = value

    @classmethod
    def get_school_name(cls):    # this is a class methid, use cls for class, self for instance
        print(cls.school)

    @staticmethod
    def info():
        print("thuis is student static method")


s1 = Student(1,2,3)
s1.m1 = 21   # illegal, we should be able to access the instance variable directly like this.
s1.get_m1()
s1.set_m1(21)
print(s1.m1)

Student.get_school_name()
Student.info()













