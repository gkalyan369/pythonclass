import re

line = "At TTS, we teach you how to perform data manipulation, " \
       "file processing and visualization using Python."

# checks for existance
found = re.search("at", line)
if found:
    print("String found")


# find all occurances
allFinds = re.findall("at", line)
for s in allFinds:
    print(s)


# find all occurances with their positions
allFinds = re.finditer("at", line)
for s in allFinds:
    posTuple = s.span()
    print(posTuple, ": ", line[posTuple[0]:posTuple[1]])


# character class
allFinds = re.findall("[plc]e", line)   
            # try with "[d-l]e" and "[a-z]e"   (char range)
            # try with "[^a-z]t"  (negated char class)
for s in allFinds:
    print(s)

