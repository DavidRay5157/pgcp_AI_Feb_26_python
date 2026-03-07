nums = [1,2,3,4,5]

it = iter(nums)
print(next(it))
print(next(it))
print(next(it))
print(it.__next__())

for i in it:
    print(i)

# create own iterator to print topten

class Topten:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration

print("custom top ten values iterable")
values = Topten()
for v in values:
    print(v)




















