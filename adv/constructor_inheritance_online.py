class A:

    def __init__(self):
        print("I am A")
    def feature1(self):
        print("I am feature1")
    def feature2(self):
        print("I am feature2")


class B(A):

    def __init__(self):
        super().__init__()    # this is calling super class constructor directly, if you remove this part also, default constructor will invoke the super class constructor.
        print("I am B")

    def feature3(self):
        print("I am feature3")


b  = B()
