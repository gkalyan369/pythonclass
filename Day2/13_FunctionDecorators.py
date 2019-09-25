# Higher order functions

### Function closures

# To print the table of a number
def tableOf(num1):
    symChar = '*'
    
    def entries(how_many, char = symChar):
        nonlocal symChar
        symChar = char
        for i in range(1, how_many+1):
            print("{} {} {} = {}".format(num1, symChar, i, num1*i))

    return entries

printTable = tableOf(10)
printTable(6, 'x')

printTable = tableOf(6)
printTable(12)



###     Decorators

def cube(num):
    return num ** 3

def twice(values):
    return values * 2


# function names can be stored in variables
gen_fun = cube
print(gen_fun(5))

gen_fun = twice
print(gen_fun([1, 2, 3, 4, 5]))


# Pass function to other functions as parameter
def function_caller(func_name, value):
    return func_name(value)

print(function_caller(gen_fun, 5))     # pass function name through a variable
print(function_caller(cube, 4))     # pass function name directly




# Dynamic functions
def func_num_multiple(num: int) -> int:      # can specify data type of argument(s) and return value

    def multiple_of(value: int):
        return num * value

    return multiple_of

multiply_numbers = func_num_multiple(4)     # similar to multiple_of(4)
print("7 * 4 = ", multiply_numbers(7))
print("7 * 4 = ", multiply_numbers("7"))      # data type specification is just for documentation!



# Decorators
def new_decorator(func):

    def wrap_func():
        print("Code would be here, before executing the func")

        func()

        print("Code here will execute after the func()")

    return wrap_func


def func_needs_decorator():
    print("This function is in need of a Decorator")

# normal function call
func_needs_decorator()

# pass function to a decorator for wrapping around
decorated_func = new_decorator(func_needs_decorator)
decorated_func()


# decorator function name can be supplied using '@' symbol
@new_decorator
def test_func_needs_decorator():
    print("This function will be wrapped in a Decorator")

@new_decorator
def sayHello():
    print("Hello")


# call decorated functions
test_func_needs_decorator()
print()
sayHello()
