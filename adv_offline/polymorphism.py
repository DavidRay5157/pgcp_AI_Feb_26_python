'''
4 types through which we can achieve polymorphism

1. Duck Typing
2. operator overloading
3. method overloading
4. method overrriding

# Duck typing :- is the concept where the type of object doesn't matter,
# what matters is whether the object has the required attribute/ behaviour or  not
class Pycharm:
    def execute(self):
        print("pychram is executing")
        print("pychram is running")

class Myeditor:
    def execute(self):
        print("My editor is executing")
        print("My editor is running")

class Vscode:
    print("vscode is running")

class Laptop:
    def code(self, ide):
        ide.execute()

ide = Vscode()
l = Laptop()
l.code(ide)

# operator overloading
a = 1
b = 2
c = a + b
print(a + b)
print(int.__add__(a,b))

print(4 > 5)

class Student:
    def __init__(self, m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):     # we're overloading the defualt add operator method
        return Student(self.m1 + other.m1, self.m2 + other.m2)

    def __gt__(self, other): return self.m1 + self.m2 > other.m1 + other.m2


s1  =Student(1,22)
s2 = Student(4,5)
s3 = s1 + s2
print(s3)
print(s3.m1, s3.m2)

if s1 > s2 :
    print("s1 wins")
else:
    print("s2 wins")


# Method overloading  => in python method overloading is not supported
class Student:

    def sum(self, a=None ,b=None , c=None):
        if a != None and b != None and c != None:
            return a + b + c
        elif a != None and b != None:
            return a+b
        else:
            return 0

s = Student()
print(s.sum(1,))
'''

# method overriding

class A:
    def show(self):
        print("A")

class B(A):
    def show(self):   # overriding
        print("B")


b = B()
b.show()


















