# this is the module we have created

def add():
    print("result 1 of add function")

def sub():
    print("result 2 of sub function")

def main():
    print(" in calc main")
    add()
    sub()

if __name__ == "__main__":  # check if the calling fucntion is this file (main) itself
    main()