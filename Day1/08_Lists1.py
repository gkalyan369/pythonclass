NumList = [10, 3, 667]
AnyElement = ["Ganesh", "43", "Dec"]
intSeq = list(range(1, 10))

joined_List = NumList + intSeq
AnyElement.sort()
print(AnyElement)
print("Total elements in joined_List are: {}, they are:".format(len(joined_List)), joined_List)


# modify element
intSeq[2] = 111
print("Elements of intSeq after modification: ", intSeq)

print("List repetion:")
print(NumList * 3)
print(AnyElement[0] * 3)

print("Value multiplication:")
print(NumList[1] * 3)


# lists once created are copies and do not refer to original lists
# observe that the contents are not modified due to intSeq modification
print("Total elements in joined_List are: {}, they are:".format(len(joined_List)), joined_List)


print("Index of 6 is: ", joined_List.index(6))
print("Value 7 appears", joined_List.count(7), "time(s)")   # how many occurrences


joined_List.append(23)
print("Elements in joined_List after append:", joined_List)

# insert
# non-existent index works like append()
AnyElement.insert(1, "Bhat")
print("After element inserted:", AnyElement)


joined_List.sort(reverse=True)
print("Elements in joined_List after sorting:", joined_List)


joined_List.reverse()
print("Elements in joined_List are reversed:", joined_List)

# remove
AnyElement.remove('43')
print("After element removed:", AnyElement)

# pop
print("Element at index 1 popped is:", AnyElement.pop(1))    # pops last element by default


# Two dimensional list
twoDList = [[1, 2, 3, 4], ['A', 'B', 'C'], 2, 5, 2]
print("\nFirst element of twoDList:", twoDList[0])
print("Value at index [1][2]:", twoDList[1][2])

print(twoDList[0].index(2))
print(twoDList.index(2, 3))
