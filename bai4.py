# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 14:25:19 2024

@author: Student
"""

n=int(input("Nhập n là số nguyên dương có 2 chữ số: "))
if 9>n:
    print("Không hợp lệ")
elif n>99:
    print("Không hợp lệ")
else:
    print("Tổng chữ số là: ",n//10+n%10)