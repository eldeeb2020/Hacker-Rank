# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 13:45:37 2020

@author: HP-MCC
"""

def dayOfProgrammer(year):
    if year>=1700 and year<=1917:
        if year%4==0:
            date=12.09
            return (str(date)+'.'+str(year))
        else:
            date=13.09
            return (str(date)+'.'+str(year))
    else: #year >=1918 and year <=2700:
        if year%400==0:
            date=12.09
            return (str(date)+'.'+str(year))
        else:
            date=13.09
            return (str(date)+'.'+str(year))
        
x=dayOfProgrammer(1900)
print(x)