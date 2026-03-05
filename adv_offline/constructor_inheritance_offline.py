class A:

    def __init__(self):
        print("i AM A")

    def feature1(self):
        print("feature1")
    def feature2(self):
        print("feature2")

class B(A):

    def __init__(self):    # this is calling the super class constructor directly, if you remove this part, default constructor will invokke the super class constructor
        super().__init__()
        print("in B")

    def feature3(self):
        print("feature3")


b = B()