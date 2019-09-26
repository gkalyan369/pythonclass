class Box:
    design = "3D"

    def __init__(self, w, h, b):
        self.width = w
        self.height = h
        self.breadth = b

    def getVolume(self):
        return self.width * self.height * self.breadth

    def displayBox(self):
        return "Width: {}, Height: {}, Breadth: {}".format(
                                        self.width, self.height, self.breadth)


class MetalBox(Box):
    def __init__(self, w, h, b, m):
        super().__init__(w, h, b)
        self.material = m

    # Method overriding
    def displayBox(self):
        ret_str = Box.displayBox(self)
        ret_str += ", Material: {}".format(self.material)
        return ret_str


b1 = Box(2, 2, 4)
print(b1.displayBox())

mb1 = MetalBox(10, 2, 3, "Copper")
print(mb1.displayBox())

print(isinstance(mb1, Box))
print(issubclass(MetalBox, Box))
print(issubclass(mb1.__class__, b1.__class__))


### Multiple inheritance in Python
class Box:
    shape = "Rectangular"

    def __init__(self, w, h, b):
        self.width = w
        self.height = h
        self.breadth = b
        self.__check = 10

    
    def printDimensions(self):
        print("w=", self.width, ", h=", self.height, ", b=", self.breadth)

    @classmethod
    def createBox(cls, dim):
        w,h,b= map(int, dim.split('-'))
        new_box = cls(w,h,b)
        return new_box

    @staticmethod
    def returnShape():
        print("Static Method: ", Box.shape)

    def __privateMethod(self):
        print("In private method")


class test:
    def __init__(self, value):
        self.value = value

    def printDimensions(self):
        print("test")
        
        
class MetalBox(Box, test):
    def __init__(self,w, h, b, typ, value):
        test.__init__(self, value)
        Box.__init__(self, w, h, b)
        self.type = typ

    def printDimensions(self):
        print("w=", self.width, ", h=", self.height, ", b=", self.breadth, ", t=", self.type, ", value=", self.value)


Box.returnShape()
b1 = Box(12, 3, 5);
b1.printDimensions()


print(MetalBox.mro())
mb1 = MetalBox(12, 3, 34, "Copper", 101)
mb1.printDimensions()
