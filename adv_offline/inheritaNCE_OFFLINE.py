class A:
    def feature1(self):
        print("i am feature1")

    def feature2(self):
        print("i am feature2")

class B(A):    # single inherotance, B is the clild, A is the parent, (A) is the syntax
    def feature3(self):
        print("i am feature3")

    def feature4(self):
        print("i am feature4")

class C(B):   # multilevel inheritance
    def feature5(self):
        print("i am feature5")

class D(B,A):  # multiple inheritance, MRO
    def feature6(self):
        print("i am feature6")



print("object if A")
a = A()
a.feature1()
a.feature2()

print("object if B")
b= B()
b.feature1()
b.feature2()
b.feature3()

print("object if C")
c = C()
c.feature1()
c.feature5()


print("object if D")
d = D()
d.feature6()
d.feature1()

print("MRO")
print(type(d).mro())






















