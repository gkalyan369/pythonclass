# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 11:28:34 2019

@author: Abridge
"""

List = [["W2342323","kalyan","kalyan@chase.com"],["E24323423","Srini","srini@chase.com"],["y123123","vas","vas@chase.com"]]

fileWritecontent = open ("Employee.txt",'w')
for i in List :
    fileWritecontent.write ("{0},{1},{2}".format(i[0:3]))
fileWritecontent.close()

with open ("Employee.txt","r") as file:
    print(file.readlines())