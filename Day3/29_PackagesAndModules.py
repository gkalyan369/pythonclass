# import py_compile
# py_compile.compile('27_APIs.py')
#
# import sys
# sys.path.insert(0, "demos.zip/lib")

import demoPack.drawings.myModule as myModule

b = myModule.Box(2, 3, 5)
print(b.displayBox())

myModule.testMod()



from demoPack.drawings import myModule

b = myModule.Box(2, 3, 5)
print(b.displayBox())

myModule.testMod()



from demoPack.drawings.myModule import testMod, Box

b = Box(2, 3, 5)
print(b.displayBox())

testMod()



from demoPack.drawings import *

b = myModule.Box(2, 3, 5)
print(b.displayBox())

Scanner.testScanner()

import demoPack.testModule
import demoPack.drawings.myModule

