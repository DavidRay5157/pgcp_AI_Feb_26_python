nums = [1,2,3,4,5]

it = iter(nums)

print(next(it))   # return 1
print(next(it))   # return 2
# alternate way to iterate the values
print(it.__next__())

print("for loop printing")
for i in [1,2,3]:
    print(i)

print("For loop internal")
it = iter([1,2,3])

while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        break


print("creating own iterable")

class Topten:
    def  __init__(self):
        self.num = 1

    def __iter__(self):    # makes the object iterable , also returns the iterator object itself.
        return self

    def __next__(self):    # returns the next value, is automatically called during iteration.
        if self.num <= 10:   # condition to stop the for loop for topten.
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration


values = Topten()
for j in values:
    print(j)









