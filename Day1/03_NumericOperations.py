# use split() function to split a string based on char(s)
num1, num2 = input("Enter two numbers ").split()

# Are num1 & num2 strings or integers?
print("{}".format(num1+num2))

# explicit conversion
num1 = float(num1)
num2 = float(num2)

# Do the arithmetic operations
sum = num1 + num2

# +, - : addition, subtraction
# *, / : multiplication, division (true division in Python 3)
# %, ** : modulus, exponentiation
# // (integer division in Python 3)

print ("Summation is:",num1+num2)
print ("Substration is:",num1-num2)
print ("Multiplication is:",num1*num2)
print ("Division is:",num1/num2)
print ("Remainder is:",num1%num2)
print ("Power is:",num1**num2)
print ("Int Division is:",num1//num2)

#   Formatted output
print("{} + {} = {}".format(num1, num2, sum))

# perform other operations below and print output
