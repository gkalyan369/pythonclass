sample_str = "  This is a python string object "


# count()	# occurrences of a substring
# index()   # index of substring; error if not found
# find()	# index of substring; -1 if not found
print("Character 'd' found ", sample_str.count("d"), " time(s)")
print("Index of first occurrence of chars 'st': ", sample_str.index("st"))
print("Index of first occurrence of char 'd' using find(): ", sample_str.find("c"))


# these functions do not modify the original string
# lstrip(), rstrip(), strip()
print("-" + sample_str.lstrip() + "-")
print("-" + sample_str + "-")

print("-" + sample_str + "-")




# upper(), lower()
sample_str = sample_str.upper()     # assign the return value to modify the original object
print(sample_str)
print(sample_str.lower())

# capitalize()		# first letter upper
print(sample_str.capitalize())

# split(), join()
words = sample_str.split(" ")
print(words)

print(" ".join('ABC'))
print(" ".join(words))



sample_str = sample_str.strip()
sample_str = sample_str.replace("python", "anaconda")
print(sample_str)

print("conda" in sample_str)


# replace()
#print(sample_str.replace("python", "VIKRAM"))

print(sample_str)
print(id(sample_str))

s = "New string"
print(id(s))
sample_str = sample_str + s
print(id(sample_str))

sample_str = sample_str.replace("PYTHON", "This is a new string")
print(id(sample_str))
print(sample_str)

