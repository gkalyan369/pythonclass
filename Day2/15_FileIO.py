f = open("sample_file.txt", "w")
f.write("First line here.\n")
f.write("and the second line\n")
#f.writelines("First line here.\nand the second line\n")
f.close()


f = open("sample_file.txt")
data = f.read()

# print char by char
for ch in data:
    print(ch)

# full file content
print(data)

# what will be the output of the following line?
data_line = f.readline()
print(data_line)

f = open("sample_file.txt")
data_line = f.readline()
print(data_line, end="")

# where is the cursor position right now?
print(f.tell())
# reset cursor to the required position
print(f.seek(0))

# read lines using for loop
for line in f:
    print(line, end="")
f.close()


# Writing lists
names_lst = ["Manjula", "Prasad", "Ganesh"]
d = open("list_data.txt", "w")
d.write("Names in the list: {}\n".format(len(names_lst)))
d.write(str(names_lst) + "\n")

# change file opening mode so that we can read the content written now 
# and execute the following two lines
#d.seek(0)
#print(d.readline())

d.close()


d = open("list_data.txt")
names = d.read()
print(names)
d.close()


# Using with block to work with files
with open("dataFile.txt", mode="w+", encoding="utf-8") as writeFile:
    writeFile.write("This file is created through Python\n")
    writeFile.write("This is the second line of the header\nand the third line and so on...")

with open("dataFile.txt", encoding="utf-8") as readFile:
    print(readFile.read())

# reset read cursor and read one line
# why will it fail?
readFile.seek(21)
print(readFile.readLine())

readFile = open("dataFile.txt", "r+")
print(readFile.closed)
print(readFile.mode)
print(readFile.name)
readFile.close()
