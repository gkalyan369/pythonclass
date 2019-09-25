# List of dictionaries
Stocks = [{"Scrip" : "ACC", "O" : 1234, "H" : 1373, "L" : 1190, "C" : 1267},
            {"Scrip" : "RIL", "O" : 934, "H" : 973, "L" : 890, "C" : 967}]

# print day high value for ACC
print(Stocks[0]["H"])


# Dictionary containing lists as values
Stocks = {"ACC" : [1234, 1373, 1190, 1267], "RIL" : [934, 973, 890, 967]}

# print day high value for ACC
print(Stocks["ACC"][1])


# Adding a list into dictionary
addr = ["B-16/63", "GB Road", "Thane", 400601]
userDetails = {"name": "Ganesh", "age": 43, "loc": "Mumbai"}

# Add the list as a value
userDetails["address"] = addr

# print dictionary contents
for user in userDetails:
    print("{}- {}".format(user, userDetails[user]))
print()


# Lists containing dictionaries
all_Users = [userDetails,
             {"name": "Rajesh", "age": 51, "loc": "Mumbai", "phone": 9987024839,
              "address":["204, Shiv Shakti CHS", "Datta Mandir Rd", "Santacruz", 400071]}]
print("List of users:")
for user in all_Users:
    print(user)
