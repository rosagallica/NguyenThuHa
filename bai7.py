# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 14:44:11 2024

@author: Student
"""

a=float(input("Số a="))
b=float(input("Số b="))
c=float(input("Số c="))
if a==0:
    if b==0:
        if c==0:
            print("Phương trình nghiệm đúng với mọi x")
        else:
            print("Phương trình vô nghiệm")
    else:
        print("Phương trình bậc nhất:", b, "x +", c, "=0")
else:
    print(a, "x^2 +", b, "x +", c, "=0")
    