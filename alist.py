import itertools
for x in range(10):
    print(type(x))


# or

for x,y in zip(range(20), itertools.count()):
    print(type(x,y))