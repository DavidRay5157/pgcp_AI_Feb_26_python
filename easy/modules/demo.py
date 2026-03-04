# import the module

from calc import *
from easy.modules import math_utils    # full qualified name for importing thge module.
#import math_utils
# from math_utils import area

import math


def func1():
    add()      # call the function add() from calc
    print("from func1")


def func2():
    print("from func2")


def main():
    func1()
    func2()


print(math_utils.add(2,3))   # acceses the module functions
print(math_utils.mul(2,3))
print(math_utils.PI)   # access the module variables also
print(math_utils.area(2))


main()
