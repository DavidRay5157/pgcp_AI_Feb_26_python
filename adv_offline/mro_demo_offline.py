'''
class A:
    def m(self):
        print("i am A")

class B(A):
    def m(self):
        print("i am B")
        super().m()

class C(A):
    def m(self):
        print("i am C")
        super().m()

class D(B,C):
    def m(self):
        print("i am D")
        super().m()

x = D()
x.m()
print(D.mro())
'''

class Animal:
    def speak(self):
        print("Animal sound")

class Mammal(Animal):
    def speak(self):
        super().speak()
        print("Mammal sounds")

class Winged(Animal):
    def speak(self):
        super().speak()
        print("winged sounds")

class Bat(Mammal, Winged):
    def speak(self):
        super().speak()
        print("Bat sound")

b = Bat()
b.speak()
print(type(b).mro())











































