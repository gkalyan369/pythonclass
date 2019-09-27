import re

line = "At TTS, we teach you how to perform data manipulation, " \
       "file processing and visualization using Python."

# ^ begins with, $ ends with
allFinds = re.findall("^[Aa]t", line)
            # try with "on." and "on.$"
for s in allFinds:
    print(s)


multiLine = '''This string is
broken into
multiple lines. 
'''

# Search in every line of a multi-line text
pattern = re.compile("(?m)^[\w]+")
allFinds = re.findall(pattern, multiLine)
for s in allFinds:
    print(s)



# Memorised blocks
# inputLine = "<name>Vikram</name><age>20</age><name>Manjula</name><age>22</age>"
inputLine = "Match for pattern and those patterns can be replaced with new text"
# pattern = re.compile("(^[\w]+)\s([\w]+)")   # first two words
pattern = re.compile(r"(pat[\w]+)(.*)(\1)")   # first two words

allFinds = re.findall(pattern, inputLine)
print(allFinds)

# memorised blocks can be created using search as well
regEx = re.search(pattern, inputLine)
print(regEx.group())
print(regEx.span())
print(regEx.group(1))
print(regEx.group(2))
print(regEx.group(3))


# memorised blocks in substitution
inputLine = re.sub(pattern, r"\3\2", inputLine)
print(inputLine)


# Named blocks
DOJ = "19 November 2001"
pattern = r"(?P<day>\d+)\s(?P<month>\w+)\s(?P<year>\d+)"
regEx = re.search(pattern, DOJ)
print("Year: ", regEx.group("year"))
print("Month: ", regEx.group("month"))
print("Day: ", regEx.group("day"))



# Look behind (?<=expr)pattern
# will match for expr and pattern sequence but returns only pattern match
animals = "1. Dog 2. cat 3. cow 4. horse"
pattern = re.compile(r"(?<=\d.\s)\w+")
allAnimals = re.findall(pattern, animals)
for n in allAnimals:
    print(n)



# Look ahead pattern(?=expr)
# will match for pattern and expr sequence but returns only pattern match
animals = "Dog, cat,   cow, horse"
pattern = re.compile(r"\w+(?=.*\s*)")
allAnimals = re.findall(pattern, animals)
for n in allAnimals:
    print(n)


# Negative look ahead and behind will look for 'NOT expr'
# Negative look ahead pattern(?!expr)
# will match pattern where expr doesn't succeed it, returns pattern match

# Negative look behind (?<!expr)pattern
# will match pattern where expr doesn't precede it, returns pattern match
