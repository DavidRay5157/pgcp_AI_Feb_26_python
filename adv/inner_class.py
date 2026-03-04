class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()

    class Laptop:
        def __init__(self):
            self.brand = "HP"
            self.cpu = "i5"
            self.ram = 12


s1 = Student("david", 1)
s2 = Student("jack", 2)
# option 1
print(s1.lap.brand)
s1.lap.brand = "Lenovo"
print(s1.lap.brand)

l1 = s1.lap
l1.cpu = "i7"
print(l1.cpu)
print(s1.lap.cpu)

# option 2
lap1 = Student.Laptop()
lap1.brand = "ACER"
print(lap1.brand)

''' you can create object of inner class inside the outer class   option 1

OR

you can create object of inner class outside the outer class by calling the name of it  option 2'''