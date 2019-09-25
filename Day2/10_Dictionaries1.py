userDetails = {}
for i in range(3):
    k = input("Enter parameter ")
    v = input("Enter value ")
    userDetails[k] = v

print(userDetails)
#userDetails[k] = input("Enter value")
#print(userDetails)



userDetails = {"name": "Ganesh", "age": 43, "loc": "Mumbai"}

# retrieve
print("User Name: ", userDetails["name"])

# update
userDetails["loc"] = "Thane"

# add new entry (key-value pair)
userDetails["phone"] = "9869484858"

print(userDetails)

# get all keys
print(userDetails.keys())

for k in userDetails.keys():
    print(k, ": ", userDetails[k])

# get all values
print(userDetails.values())

# check for existence
print("loc as key exists:", "loc" in userDetails)
print("address as key exists:", "address" in userDetails)


# iterate through all key-value pairs
for key, value in userDetails.items():
    print("{}: {}".format(key, value))


# returns the value. If not found, returns message
print(userDetails.get("contact", "Contact doesn't exists. Check if its stored as phone"))


# remove key-value pair
del userDetails["phone"]
print("phone entry deleted.")

print(userDetails)

# returns keys by default
print("Contents of userDetails")
for user in userDetails:
    print(user)
#    print("{}- {}".format(user, userDetails[user]))


# clears the dictionary
userDetails.clear()
print("Contents of userDetails after clear")
for user in userDetails:
    print(user)


from collections import Counter
ls = [2, 3, 45, 5, 2, 4, 1, 3, 5, 1, 2, 455]
ct = Counter(ls)
print(ct)
print(ct.most_common())
print(ct.values())
print(ct.items())
ct.clear()
print(ct)

l = ["Ravi", "Manoj", "Pallavi", "Ravi", "Vijay"]
ct = Counter(l)
print(ct)
