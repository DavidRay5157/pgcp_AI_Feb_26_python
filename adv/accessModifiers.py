# in python we dont have access modifiers like we have in other languiages like java, c++
'''
class Person:
    def __init__(self, name):
        self.name = name    # this is public access

    def greet(self):
        print("Hello " , self.name)


p = Person("Jack")
print(p.name)
p.greet()

class Person:
    def __init__(self, name):
        self._name = name    # this is protected access

    def greet(self):
        print("Hello " , self._name)


p = Person("Jack")    # still print it.
print(p._name)
p.greet()
'''

class Person:
    def __init__(self, name):
        self.__name = name    # this is private access

    def greet(self):
        print("Hello " , self.__name)

    def get_name(self):
        return self.__name


p = Person("Jack")    # still print it.
#print(p.__name)   # throw error
print(p.get_name())