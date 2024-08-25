# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 15:21:28 2024

@author: Student
"""

import math
a = float(input("Nhập số a:"))
b = float(input("Nhập số b:"))
if a < 0 or b < 0 or a==b:
    print("a và b phải là số không âm và khác nhau")
tu_so1 = math.sqrt(a) - math.sqrt(b)
mau_so1 = math.pow(a, 0.25) - math.pow(b, 0.25)
phan_so1 = tu_so1/mau_so1

tu_so2 = math.sqrt(a) + math.pow(a*b, 0.25)
mau_so2 = math.pow(a, 0.25) + math.pow(b, 0.25)
phan_so2 = tu_so2/mau_so2

B = phan_so1 - phan_so2
print("Giá trị của B là: ",B)
