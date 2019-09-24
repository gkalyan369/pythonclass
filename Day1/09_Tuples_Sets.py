# Tuples
empty_tuple = ()
emp_IDs = 'P873874', "E948573",  46, "P248723"
# emp_IDs = ('P873874', "E948573", 46, "P248723")      # both are fine
name_tuple = tuple("Ganesh Bhat")

print(emp_IDs)
print(name_tuple)

# a list
name_list = ["Ganesh", "Manoj", "Pallavi", "Ravi", "Vijay"]

# print object types
print(type(empty_tuple))
print((type(emp_IDs)))
print((type(name_list)))
print(type(emp_IDs[1]) is int)

# Can not modify a tuple
# empty_tuple[0] = "Srividya"


print("Empty tuple:", empty_tuple)
print("tuple from a string:", name_tuple)

# create a tuple from a list
empty_tuple = tuple(name_list)
print(empty_tuple)

# print tuple contents
print("Contents of tuple created from list:")
for el in empty_tuple:
    print(el)

print("Contents of Emp_IDs tuple:")
print(emp_IDs)

print(emp_IDs.index("P248723"))
print(name_tuple.count('h'))
print(len(name_tuple))
print(max(name_tuple))

# problems with different object types
print(min(emp_IDs))

all_entries = empty_tuple + emp_IDs
print(all_entries)


# unpacking tuple
v1, v2 = emp_IDs[0:2]
print(v1, " ", v2)
#print(emp_IDs)


# Sets
empty_set = set()
empty_set.add(234)
print(empty_set)

numbers = {25, 553, 863, 2, 634}
numbers.remove(863)     # raises LookupError if not found
numbers.discard(863)    # removes if found, no error if not found

numbers.add(25)
print(len(numbers))

emps = ["P12", "E34", "P17", "P12"]
emps_set = set(emps)
print("P12" not in emps_set)

l = list(emps_set)
print(l[2])

# Does not support indexing
# print(numbers[1])

odd_nums = [23, 53, 79, 91, 13, 7]

numbers.update(odd_nums)
print(numbers)

print(numbers.pop())
n1 = numbers.copy()
print(n1)

odd_nums.clear()
print(odd_nums)
