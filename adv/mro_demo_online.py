'''
class A:
    def m(self):
        print("I am A")

class B(A):
    def m(self):
        print("I am B")
        super().m()

class C(A):
    def m(self):
        print("I am C")
        super().m()

class D(B,C):
    def m(self):
        print("I am D")
        super().m()



x = D()
x.m()
print(type(x).mro())
'''

class Animal:
    def speak(self):
        print("Animal sounds")

class Mammal(Animal):
    def speak(self):
        super().speak()
        print("Mammal sounds")

class Winged(Animal):
    def speak(self):
        super().speak()
        print("Winged sounds")


class Bat(Mammal, Winged):
    def speak(self):
        super().speak()
        print("Bat Sound")


b = Bat()
b.speak()
print(Bat.mro())





















