# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 10:05:18 2019

@author: Abridge
"""
employeeList=[]
for value in range(1,6):
    employeeListString=input("Enter  alpha numberic Employee ID:") 
    employeeList.append(employeeListString)
#employeeList=employeeListString.split()

for ite in employeeList :
    print ("Employee id is:", ite)