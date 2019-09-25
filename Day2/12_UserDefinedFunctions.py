## Function definition
def getSum(num1, num2 = 0):
    sum = num1+num2
    return sum

s = getSum(15, 8)
print("Sum of 15 and 8 is: ", s)

# Note: if there is no explicit return statement in a function,
# it returns None (so make sure to return a value from a function


## Use of local and global variables
## global variable (defined outside any function)
sum = 0

def getTotal(num1, num2):
    global sum
    sum = num1+num2

    # if you want to use local as well as global, use globals()['varname']
    # globals()['sum'] = 1234

    print('Value of sum variable inside function is: ', sum)
    return sum

s1 = getTotal(5, 8)
print("Sum of 5 and 8 is: {} and global variable value is: {}".format(s1, sum))



# If you pass a list to a function, you can modify the contents of it
# but if you assign a new list to it, original list will not be affected
num_lst = [1, 2, 3]

def ListScope(lst):
    print("Value before modification: ", lst[0])
    lst[0]=4
    print("Value after modification: ", lst[0])
    
    # what is the result of this statement?
    lst = [10, 20, 30, 40]


print("Initial value: ", num_lst[0])
ListScope(num_lst)
print("List contents after modification: ", num_lst)

