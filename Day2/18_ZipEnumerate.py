###     Zip
# Two equal length lists
L1 = [1, 2, 3]
L2 = [4, 5, 6]
L_Result = zip(L2, L1)
print(list(L_Result))

# Three equal length lists
L1 = [1, 2, 3]
L2 = [4, 5, 6]
L3 = [7, 8, 9]
L_Result = zip(L1, L2, L3)
print(list(L_Result))

# Two non-equal length lists
L1 = [1, 2, 3]
L2 = [4, 5]
L_Result = zip(L1, L2)
print(list(L_Result))
print(list(zip(L1)))


# Two dictionaries
D1 = {"x": 1, "y": 2}
D2 = {"p": 4, "q": 5}
D_Result = zip(D1, D2)
print(list(D_Result))

D_Result = zip(D1.keys(), D2.values())
print(list(D_Result))




###     Enumerate
months = ["Apr", "May", "Jun", "Jul",
          "Aug", "Sep", "Oct", "Nov", "Dec", "Jan", "Feb", "Mar"]

for (m_no, mon) in enumerate(months):
   print(m_no, mon)

for (m_no, mon) in enumerate(months, start=1):
   print(m_no, mon)



###     any() and all()
bool_list = [True, False, True, True]
print("Are there any True values in the list? ", any(bool_list))
print("Are all the elements in the list True? ", all(bool_list))
