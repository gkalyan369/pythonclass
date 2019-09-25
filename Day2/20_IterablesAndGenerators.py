###     Iterables and Iterators

iterString = iter("String of Characters")
print("First char: ", next(iterString))
print("Next char: ", next(iterString))


# Custom Iterators
class HexaDecimal:
    def __init__(self):
        self.values = "0123456789ABCDEF"
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.values)-1:
            raise StopIteration
        self.index += 1
        return self.values[self.index]


hex1 = HexaDecimal()
obj1 = iter(hex1)

print(next(obj1))
print(next(obj1))

for h in obj1:
    print(h)


# Custom Iterators with different Iterable and Iterator classes
class HexaDecimalData:
    def __init__(self):
        self.values = "0123456789ABCDEF"


class Hex:
    def __init__(self, Hx):
        self.HD = Hx
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.HD.values)-1:
            raise StopIteration
        self.index += 1
        return self.HD.values[self.index]


hexD = HexaDecimalData()
print(hexD.values)
h1 = Hex(hexD)

print(next(h1))
print(next(h1))

for h in h1:
    print(h)



###     Generators

# List creates all the values at once
# i = [x for x in range(int(10e+300))]
# print(i[0])

# Generators doesn't create whole list, instead generates one value for each call
# Generator comprehensions
even_numbers = (x * 2 for x in range(int(10e+300)))
print(next(even_numbers))
print(next(even_numbers))


# syntax looks like a tuple but its a generator
# use explicit typecast to tuple to make it a tuple
t = (x for x in range(10))
print(type(t))
# if its a generator, get next value using next()
print(t)


def cube_gen(num):
    for n in range(1, num):
        yield n**3

o = cube_gen(10)
print(next(o))
print(next(o))

#o2 = cube_gen(10)
for value in o:
    print(value)


### Practice: Create an iterable Employees class returning empID on each next() call
    
    