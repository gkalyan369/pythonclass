import sys
import numbers

'''
Here is an example of multi-line comment.
following line is a print function call
using parentheses in Python 3
'''

print(sys.version, sys.version_info)


# formatted output in Python 3
print("{} on {}".format(sys.version, sys.version_info))

# print integer variable type
v1 = 10
v2 = 3.456
s = "Variable types in Python"
y= True

print("type of v1: ", type(v1))
print("type of v2: ", type(v2))
print("type of s: ", type(s))
print("type of y: ", type(y))

# write code blocks in Python using indentation
if issubclass(type(v2), numbers.Number):
    print("\tThis is part of if block.")
    if (v2 == 3.456):
        print ("This is inside the nested block")
    print("\tYou can write any number of lines of code as part of a block")
    print("\tby ensuring they are properly aligned.")
    # all lines of the block are aligned together

# following lines are part of the outer block
# crete a boolean variable
v3 = True
print("type of v3: ", type(v3), "and its value is: ", v3)

# additional parameters in format are ignored
print("Value of variable 1 is: {} and variable 2 is: {}".format(v1, v2, v3))

# positionally access format arguments
print("Value of variable 3 is: {2} and variable 1 is: {0}".format(v1, v2, v3))

# you can split the strings to better manage formatting, if needed
print("Type of variable 1 is: {}".format(v1), "and variable 2 is: {}".format(v2, v1, v3))

b = None    # create a variable as a placeholder but won't have any value
if (b == None):
    print ("Condition satified")
