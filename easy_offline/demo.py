# import the module

# import calc
from calc import *
import math

def func1():
    sub()    # main() cannot be called becuse it will call this instance main function which will throw recursion error
    print("from func1")


def func2():
    print("from func2")

def main():
    func1()
    func2()

main()