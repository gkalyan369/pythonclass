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
#        print("Class Method: ", cls.shape)

    @staticmethod
    def returnShape():
        print("Static Method: ", Box.shape)

    def __privateMethod(self):
        print("In private method")

    def __str__(self):
        return "w=" + str(self.width) + ", h=" + str(self.height) + ", b=" + str(self.breadth)
    
b = Box.createBox('2-3-4')
print(b)
Box.returnShape()
b1 = Box(12, 3, 5);
Box.printDimensions(b1)
#print(b1.__check)
b1.__privateMethod()
