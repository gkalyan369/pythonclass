import xml.etree.ElementTree as etree

# parse xml file
tree = etree.parse("bookstore.xml")
root = tree.getroot()
print("Root element: ", root)

# no of child elements of root
print("Root has {} child elements and they are:".format(len(root)))

# print all child elements
print(root.tag)
for c in root:
    print("\t", c.tag, end="")  # element name
    print(c.attrib)     # attribute of an element
    for cel in c:
        print("\t\t", cel.tag)


# inspect attribute using root
print(root[0][0].attrib)


print(root.findall('book'))     # only in direct child elements
print(tree.findall('.//author'))     # only in direct child elements

