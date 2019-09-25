# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 10:05:18 2019

@author: Abridge
"""
employeeList=[[],[],[]]
for value in range(1,9):
    employeeListString=input("Enter  alpha numberic Employee ID:")
    if (employeeListString.isdigit()):
        employeeList[0].append(employeeListString)
    elif (employeeListString.isalnum()):
        if (employeeListString.isalpha()):
         employeeList[2].append(employeeListString)
        else:
            employeeList[1].append(employeeListString)
#    else :
#        employeeList[2].append(employeeListString)
#    elif (employeeListString.isalpha()):
#        if (not employeeListString.isalnum()):
#            employeeList[2].append(employeeListString)
#        else:
#            employeeList[1].append(employeeListString)
#employeeList=employeeListString.split()

for ite in employeeList :
    print ("Employee id is:", ite)
    
#print ("Employee id's are {0},{1},{2},{3},{4}".format(employeeList[0],employeeList[1],employeeList[2],employeeList[3],employeeList[4]),sep="\t")