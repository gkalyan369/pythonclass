# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 10:14:44 2019

@author: Kalyan G
"""

num1,num2=input("Enter two numbers:").split()
num1=int(num1)
num2=int(num2)
num3=num1+num2

print("summation of {} and {} is {}".format(num1,num2,num3))
print ("Multiplication of {} and {} is {}".format(num1,num2,num1*num2))
print ("True Division of {} and {} is {}".format(num1,num2,num1/num2))
print (type(num1/num2))
print ("Division of {} and {} is {}".format(num1,num2,num1//num2))
print (type(num1//num2))
print ("Division of {} and {} is {}".format(num1,num2,num1%num2))
print (type(num1%num2))
print ("Division of {} and {} is {}".format(num1,num2,num1**num2))
print (type(num1**num2))