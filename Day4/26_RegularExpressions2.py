'''
# Meta characters
Backspace: \b
Form feed: \f
Carriage return: \r
Tab: \t
Vertical tab: \v


A digit: \d or [0-9]
Not a digit: \D or [^0-9]
A word: \w  or [a-zA-Z0-9_]
Not a word: \W  or [^a-zA-Z0-9_]
Occurances:
 three digits: \d{3}
 three to six digits: \d{3,6}
Any space char: \s  or [\f\r\n\t\v]
Not a space: \S     or [^\f\r\n\t\v]


# Multiples
One or more: +
zero or more: *
zero or one: ?


OR: use | between patterns/parts of pattern
'''


import re

# Search and replacement
searchStr = "Employee id of Vikram is P350394 and he works in retail banking"

# two ways to pattern searching
# one using re.search function
m = re.search("[A-Z]\d{3,6}", searchStr)
print(m.span())
# print(searchStr[m.span()[0]:m.span()[1]])
# re.findall("[A-Z]\d{3,6}", searchStr)


# second by compiling a search pattern and applying it on the string
pattern = re.compile("[A-Z]\d{3,6}")
m = pattern.search(searchStr)
print(m.span())


# substitute 
# replace all occurances of 'in' with 'at'
pattern = re.compile("i.")
# if number of occurances is set, those many matches will be replaced
# default is all occurances
searchStr = pattern.sub("AT", searchStr, 2)
print(searchStr)


# Raw strings or string literals in search
# Use escape char to print back slash literally
searchStr = "Some languages use escape char \\ to embed backslash \\."
print(searchStr)

found = re.search("\\\\", searchStr)   # or use r"\\"
if found:
    print("Escapse or newline chars found")


# multi line text can also be represented using three quotes
searchStr = '''Some languages allow
spanning text on
multiple lines
'''

print(searchStr)

pattern = re.compile("\s")
searchStr = pattern.sub("-", searchStr)
print(searchStr)



# Greedy and lazy match
xmlString = "<name>Vikram</name><name>Manjula</name>"
pattern = re.compile("<name>.*</name>")     # ".*" is greedy, ".*?" is lazy
allNames = re.findall(pattern, xmlString)
for n in allNames:
    print(n)


# using * will look for largest match
# using ? will stop match at first occurance (smallest match)
# ? can be used with + and {} as well

