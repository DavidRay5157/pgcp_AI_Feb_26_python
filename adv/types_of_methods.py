class Student:

    school = "cdac"   # class variable

    def __init__(self, m1, m2 ,m3):
        self.m1 = m1    # instance variables
        self.m2 = m2
        self.m3 = m3

    def avg(self):     # instance method, because we have self
        return (self.m1 + self.m2 + self.m3) / 3

    # this is design pattern so outside objects cannot direclty access instance variables.
    def get_m1(self):   # getter method, in python we call this accessor
        return self.m1

    def set_m1(self, value):    # setter method, in python we call this mutators
        self.m1 = value

    @classmethod       # this is decorator , use to define class method
    def get_school_name(cls):    # TASK TO DO -> take a parameter to update the class variable from this function.
        print(cls.school)


    #static method
    @staticmethod
    def info():
        print("this is student info static method")


s1 = Student(1,2,3)
s2 = Student(2,6,5)
s1.m1 = 4   # this is illegal to do, we should not directly access the instance variables
print(s1.avg())

Student.get_school_name()

Student.info()

s2.info()