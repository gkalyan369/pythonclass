age = 2

if age >= 18:
    print("Go cast your vote!")
elif age >= 5:
    print("Underage! you can't vote.")
else:
    print("Toddler! keep home.")

if age >= 21:
    print("You can contest election.")

#if age >= 18 and age < 21:
#    print("Wait till 21 to contest election.")

# same can be written using chained comparison operator
if 18 <= age < 21:
    print("Wait till 21 to contest election.")
