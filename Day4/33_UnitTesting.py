import unittest
import demoPack.drawings.myModule as mm

class myModuleTest(unittest.TestCase):

    def setUp(self):
        pass
    
    def test_getVolume(self):
        b1 = mm.Box(2, 3, 4)
        self.assertEqual(24, b1.getVolume())
        
    def test_displayBox(self):
        b1 = mm.Box(2, 3, 4)
        self.assertEqual("Width: 2, Height: 3, Breadth: 4", b1.displayBox())
        
        
        # other tests
        #self.assertTrue()
        #self.assertFalse()
        #self.assertRaises()
        
if __name__ == "__main__":
    unittest.main()

