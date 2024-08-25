# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 17:58:48 2024

@author: Ha
"""

string = "i'm a cat"
titlecase = string.title() 
print(titlecase)
uppercase = string.upper()
print(uppercase)
first_upper = string[0] + string[1] + string[2].upper() + string[3:7] + string[7:9].upper()
print(first_upper)
capitalize = string.capitalize()
print(capitalize)

