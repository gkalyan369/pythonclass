## Function with variable number of arguments
def sumNumbers(*args):
    s = 0
    for n in args:
        if type(n) is list:
            for i in n:
                s += i
        if type(n) is int:
            s += n
    return s


num_lst = [10, 20, 30, 456, 45, 13]
result = sumNumbers(100, num_lst, 1000)
print("Sum of numbers is: ", result)


def printUserDetails(**kwargs):
    for k, v in kwargs.items():
        print(v)

printUserDetails(Scrip = "ACC", O = 1282, H = 1376, L = 1190, C = 1287)
printUserDetails(Name = "Ganesh", Age = 43)



## Lambda expressions
getSum = lambda num1, num2: num1 + num2
s = getSum(12, 45)
print(s)

square = lambda num: num ** 2
print(square(3))

sum = lambda n1, n2: n1 + n2
print(sum(10, 23))

rev = lambda s: s[::-1]
print(rev('Hello'))



# Conditionals in lambda expressions
can_vote = lambda age: True if age >= 18 else False
print("Can vote: ", can_vote(13))
