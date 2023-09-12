# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 11:31:46 2023

@author: natha
"""
"""

Write a Python program to print the following string in a specific format (see the output).
Sample String :
 "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"



"""
print("Twinke,twinkle,little star, \n\tHow I wonder what you are!\n\t\tup above the world so high, \n\t\tLike a diamond in the sky.\ntwinckle,twinckle little star,\n\tHow I wonder what you are.")

"""
Write a Python program to find out what version of Python you are using.

"""
import sys
print("Python version")
print(sys.version)
print("Version info.")
print(sys.version_info)

"""
Write a Python program to display the current date and time.
"""

import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))




print("metaverse")
_a=input("Enter your name?")
print("Name=",_a)
b=int(input("Enter your number?"))
print("Number=",b)
c=float(input("Enter a decimal number "))
print("Number=",c)

First=input("Put Your first name:")
Last=input("Put ur last name cuh:")
print("hello",Last,"",First)

from math import pi
r = float(input("input the radius of the circle:"))
print("Area=",pi* r**2)