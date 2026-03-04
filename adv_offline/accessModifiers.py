# in python we ddont have access modifiers like java, c++
'''
class Person:
    def __init__(self, name):
        self.name = name   # this is by default public

    def greet(self):
        print("Hello ", self.name)


p = Person("John")
print(p.name)
p.greet()

class Person:
    def __init__(self, name):
        self._name = name   # this is by protected

    def greet(self):
        print("Hello ", self._name)


p = Person("John")
print(p._name)
p.greet()
'''

class Person:
    def __init__(self, name):
        self.__name = name   # this is by private

    def greet(self):
        print("Hello ", self.__name)

    def get_name(self):
        return self.__name


p = Person("John")
#print(p.__name)  # show error for private variable
print(p.get_name())
p.greet()