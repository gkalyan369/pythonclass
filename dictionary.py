# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 12:44:52 2019

@author: Abridge
"""

dictionary={112:"Kalyan",212:"Srini",1221:"vas"}

#print ("Keys are",dictionary.keys)
for i in dictionary :
    print (i,"Value is:",dictionary[i])
#print ("Dict items are",dictionary.items)
    
dictionary[1]="Kalyan Srinivas"
print ("New Value is:",dictionary)

dictionary[112] ="Shivas"
print ("recent value is:",dictionary)

del dictionary [112]

print (dictionary)
