'''
in python we can achieved by 4 ways :-

1. duck typing
2. operator overloading
3. method overloading
4. method overriding
'''

# Duck Typing = is the concept where the type of the object doesn't matter, what matters is whether the object has the required method/ behavior or not
'''
class Pycharm:
    def execute(self):
        print("compiling by pychram")
        print("pycharm is running")
        
class Myeditor:
    def execute(self):
        print("My editor is running")
        print("myeditor is compiling")
        
class Laptop:
    def code(self, ide):
        ide.execute()
        
ide  = Pycharm()
l = Laptop()
l.code(ide)

# operator overloading

a = 1
b = 2
c = a + b
print(c)
print(5>6)
print(int.__add__(a,b))

class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):    # we're overloading the default add operator method
        return Student(self.m1 + other.m1, self.m2 + other.m2)

    def __gt__(self, other): return self.m1 + self.m2 > other.m1 + other.m2
    # is a special method, also known as "dunder" (double underscore) or magic method, that implements the greater-than operator (>)



s1 = Student(1,21)
s2 = Student(3,4)

s3 = s1 + s2
print(s3.m1, s3.m2)

if s1 > s2:
    print("s1 wins")
else:
    print("s2 wins")



# method overloading alternate way, because in python it is not supported.
class Student:
    def  __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self,a= None , b=None, c=None):
        if a != None and b != None and c != None:
            return a + b + c
        elif a != None and b != None:
            return a + b
        else:
            return 0

s = Student(1,21)
print(s.sum(1,3,4))
'''
# this is method overriding
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):    # overriding
        print("B")


obj = B()
obj.show()




















