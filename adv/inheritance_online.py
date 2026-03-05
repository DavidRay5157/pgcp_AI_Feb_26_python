class A:    # parent class
    def feature1(self):
        print("i am feature1")

    def feature2(self):
        print("i am feature2")


class B(A):   # single inheritance, B is child, (A) is inheritance syntax of parent A.
    def feature3(self):
        print("i am feature3")

    def feature4(self):
        print("i am feature4")

class C(B):    # multi level inheritance
    def feature5(self):
        print("i am feature5")

class D(B,A):
    def feature6(self):
        print("i am feature6")

# create object
a1 = A()
a1.feature1()
a1.feature2()
print("after A class")
b1 = B()
b1.feature1()
b1.feature2()
b1.feature3()
b1.feature4()
print("after B class")
c1 = C()   # object is only for C
c1.feature1()  # this is feature of class A
c1.feature2()
c1.feature3()  # feature of class B
c1.feature4()
c1.feature5()
print("after C class")
