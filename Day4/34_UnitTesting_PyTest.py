import pytest
import demoPack.drawings.myModule as mm

class TestMyModule:

    def test_getVolume(self):
        b1 = mm.Box(2, 3, 4)
        assert 24, b1.getVolume()
    
    def test_displayBox(self):
        b1 = mm.Box(2, 3, 4)
        assert "Width: 2, Height: 3, Breadth: 4", b1.displayBox()
    
