# The Bytes Type
# The bytes type in Python is immutable and stores a sequence of values
# ranging from 0-255 (8-bits).
# You can get the value of a single byte by using an index like an array,
# but the values can not be modified.
# Create empty bytes
empty_bytes = bytes(4)
print(type(empty_bytes))
print(empty_bytes)


# The Bytearray Type
# To create a mutable object you need to use the bytearray type.
# With a bytearray you can do everything you can with other mutables
# like push, pop, insert, append, delete, and sort.
# Cast bytes to bytearray
mutable_bytes = bytearray(b'\x00\x0F')
print(len(mutable_bytes))
print(mutable_bytes)

# Bytearray allows modification
mutable_bytes[0] = 255
mutable_bytes.append(255)
print(mutable_bytes)

# Cast bytearray back to bytes
immutable_bytes = bytes(mutable_bytes)
print(immutable_bytes)

# Writing Bytes to a File
with open("test_file.dat", "wb") as binary_file:
    # Write the bytes to file
    data = binary_file.write(immutable_bytes)

# Reading Bytes From a File
with open("test_file.dat", "rb") as binary_file:
    # Read the whole file at once
    data = binary_file.read()
    print(data)

    # Seek position and read N bytes
    binary_file.seek(0)  # Go to beginning
    couple_bytes = binary_file.read(2)
    print(couple_bytes)


# Integer to Bytes
i = 16

# Create one byte from the integer 16
single_byte = i.to_bytes(1, byteorder='big', signed=True)
print(single_byte)

# Create four bytes from the integer
four_bytes = i.to_bytes(4, byteorder='big', signed=True)
print(four_bytes)

# Compare the difference to little endian
print(i.to_bytes(4, byteorder='little', signed=True))

# Create bytes from a list of integers with values from 0-255
bytes_from_list = bytes([255, 254, 253, 252])
print(bytes_from_list)

# Create a byte from a base 2 integer
one_byte = int('11110000', 2)
print(one_byte)

# Print out binary string (e.g. 0b010010)
print(bin(22))


# Bytes to Integer
# Create an int from bytes. Default is unsigned.
some_bytes = b'\x00\xF0'
i = int.from_bytes(some_bytes, byteorder='big')
print(i)

# Create a signed int
i = int.from_bytes(b'\x00\x0F', byteorder='big', signed=True)
print(i)

# Use a list of integers 0-255 as a source of byte values
i = int.from_bytes([255, 0, 0, 0], byteorder='big')
print(i)


# Text Encoding
# Binary to Text
binary_data = b'I am text.'
text = binary_data.decode('utf-8')
print(text)

binary_data = bytes([65, 66, 67])  # ASCII values for A, B, C
text = binary_data.decode('utf-8')
print(text)

# Text to Binary
message = "Hello"  # str
binary_message = message.encode('utf-8')
print(type(binary_message))  # bytes

