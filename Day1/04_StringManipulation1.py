# index       0    5  8 10     17     24
sample_str = "This is a python string object"


print("No. of chars in the string is: ", len(sample_str))
print("First char of the string: ", sample_str[0])
print("Last char of the string: ", sample_str[-1])  # very useful

# string repetition operator
print("Hello " * 4)

# string slice
print("Characters between index 10(included) and 17(excluded): '{}'".format(sample_str[10:17]))
print(sample_str[:])
print(sample_str[-3:-1])

# Use step frequency operator
print(sample_str[::1])  # step frequency of 1
print(sample_str[5::2])  # step of 2 chars, starting from index 5
print(sample_str[::-1])     # reverse a string
print(sample_str[17::-2])     # reverse a string with 2 chars step


# unicode and char conversions
# using '+' operator on strings; both operands must be strings, convert if not
print("Unicode value of 'A': " + str(ord('A')))
print("Char representing unicode 65 is: ", chr(65))


# use a string in for loop to access each char
for c in sample_str:
    print(c, ",", end="", sep=" ")
print("")


# string objects are immutable; cannot modify
# uncomment 2 statements below and execute; understand the error generated.
#sample_str[0] = "t"
#print(sample_str)


# isalnum()		# alpha numeric
print("alphanumeric: ", "P235".isalnum())

# isalpha()
print("alphabet: ", "h3".isalpha())

# isdigit()
print("digit: ", "357".isdigit())

# islower(), isupper()
print("uppercase letter: ", "R".isupper(), ", lowercase letter: ", "#".islower(), sep="")

# isspace()
print("space: ", "\t".isspace())

# Try it yourself
# print the third last character


# print the no of times char 'd' is found


# print the char found after 'y'
