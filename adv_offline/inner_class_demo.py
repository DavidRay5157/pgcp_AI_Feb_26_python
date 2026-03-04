class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.lap = self.Laptop()  # create object of laptop while creating object of student

    class Laptop:
        def __init__(self):
            self.brand = "HP"
            self.cpu = "i5"


s1 = Student("david", 60)
s2 = Student("Patel", 10)
s1.lap.brand = "ACER"
print(s1.lap.brand)
print(s2.lap.brand)

l1 = s1.lap
print(l1.cpu)

lap1 = Student.Laptop()
lap1.brand = "asus"
print(lap1.brand)











