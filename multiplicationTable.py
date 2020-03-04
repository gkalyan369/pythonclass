# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 18:32:23 2020

@author: Kalyan G
"""

tablePrint = input ("Enter the number for which table to be printed: ")
number = int( input ("Depth of the table needs to be printed: "))
for i in range (1,number+1):
    print ("{} * {} = {}".format(i,tablePrint,i*int(tablePrint)))