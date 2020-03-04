# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 19:42:37 2020

@author: Kalyan G

AIM of this below function is to take in out from user prompt and print the traingle as sated in the problem statemnet


Below Python will only excute on Python 3.7

"""

def printTraingle(n):
    i=0
    for i in range (0,n):
        for j in range (0,i+1):
            print ("*" ,end="")
        print("\n")
inputNumber= input ("Enter the Depth of the traingle you want to print:")
printTraingle(int(inputNumber))