class Animal:
    count = 0

    def __init__(self, wt, lg):
        self.weight = wt
        self.nooflegs = lg

    def setWeight(self, w):
        self.weight = w

    def getWeight(self):
        return self.weight

#    def __repr__(self):
#        return "REPR: Weight: " + str(self.weight) + " and No. of legs: " + str(self.nooflegs)

#    def __str__(self):
#        return "STR: Weight: " + str(self.weight) + " and No. of legs: " + str(self.nooflegs)


print(Animal.count)
print(a)
a = Animal(25, 4)
Animal.count += 1
print(a.getWeight())
a.setWeight(68)
print(a.getWeight())
print(a.count)

b = Animal(38, 2)
print(b.nooflegs)



class Box:
    design = "3D"

    def __init__(self, w, h, b):
        self.width = w
        self.height = h
        self.breadth = b

    def getVolume(self):
        # self.color = "red"      # though it works, not a good thing
        return self.width * self.height * self.breadth

    def displayBox(self):
        return "Width: {}, Height: {}, Breadth: {}".format(
                                        self.width, self.height, self.breadth)

    def setBoxFeatures(self, *args):
        if len(args) == 1:
            self.width = args[0]
        elif len(args) == 2:
            self.width, self.height = args[0:2]
        else:
            self.width, self.height, self.breadth = args[0:3]


b1 = Box(10, 2, 3)
print(b1.getVolume())
b1.setBoxFeatures(20)
print(b1.getVolume())

# print(b1.color)
print(b1.displayBox())
print(Box.design)


# No private variables
print("Width = " + str(b1.width))
