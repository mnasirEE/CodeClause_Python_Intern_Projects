
"""
Created on Tue Sep  5 21:43:16 2023

@author: M.Nasir
"""


''' Task 2 : Calculator in Python 
'''

import numpy as np
    
def add(a,b): # add two numbers 
    return np.around(a + b,3)   # return result with 3 decimal places

def sub(a,b): # subtract two numbers
    return np.around(a - b,3)   # return result with 3 decimal places

def mul(a,b): # multiply two numbers
    return np.around(a * b,3)  # return result with 3 decimal places

def div(a,b): # divide two numbers
    return np.around(a / b,3) # return result with 3 decimal places

a = float(input("Enter 1st number: "))
b = float(input("Enter 2nd number: "))

# Printing Addition of two numbers
print("The Addition of two numbers is", add(a,b))
# Printing Subtraction of two numbers
print("The Subtraction of two numbers is", sub(a,b))
# Printing Multiplication of two numbers
print("The Multiplication of two numbers is", mul(a,b))
# Printing Division of two number
print("The Division of two numbers is", div(a,b))

     