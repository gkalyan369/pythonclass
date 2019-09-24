for i in range(14, 0, -1):
    if i == 14:
        break
    elif i == 9:
        continue
    print(i)
else:
    print("Else of for loop")

print("Loop ended")



num1, oper, num2 = input("Enter operation to perform ").split()

num1 = eval(num1)
num2 = eval(num2)

#   Do the arithmetic operations based on operator
# +, -, *, /
if oper == "+":
    print("{0} + {1} = {2}".format(num1, num2, num1+num2))
elif oper == "-":
    print("{} - {} = {}".format(num1, num2, num1 - num2))
elif oper == "*":
    print("{} * {} = {}".format(num1, num2, num1 * num2))
elif oper == "/":
    print("{} / {} = {}".format(num1, num2, num1 / num2))
else:
    print("Enter one of +, -, *, / operators")

