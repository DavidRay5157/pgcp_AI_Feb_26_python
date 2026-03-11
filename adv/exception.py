
try:
    x = 1/0
    number = int(4)
except (ZeroDivisionError, ValueError):
    print("hello multiple exceptions")
except Exception as e:
    print(e)
else:
    print("into else block")
finally:
    print("in finally block")
    raise NameError("An exception occured!")



    #x = 1/0   # program has exited from this line
print("prgram is running upto here")
