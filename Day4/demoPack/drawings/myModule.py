
def testMod():
    print("Module name: ", __name__)


class Box:
    design = "3D"

    def __init__(self, w, h, b):
        """ 
        The constructor for the Box class. 
  
        Parameters: 
            w (int): The width of box. 
            h (int): The height of box.
            b (int): The breadth if box.
        """
        
        self.width = w
        self.height = h
        self.breadth = b

    def getVolume(self):
        """ 
        The function to return Box volume. 
  
        >>> b1 = Box(2, 3, 4)
        >>> b1.getVolume()
        24
        
        Returns: 
            vol (int): An integer that's the volume of the box. 
        """
        
        vol = self.width * self.height * self.breadth
        return vol 

    def displayBox(self):
        return "Width: {}, Height: {}, Breadth: {}".format(
                                        self.width, self.height, self.breadth)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    