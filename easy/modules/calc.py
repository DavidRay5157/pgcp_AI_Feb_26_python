# this is the module we have created

def add():
    print("result 1 of add")


def sub():
    print("result 2 of sub")


def main():
    print("in calc main")
    add()
    sub()


if __name__ == "__main__":     # check the calling function is main or not, if yes run the main() to show all output.
    main()
