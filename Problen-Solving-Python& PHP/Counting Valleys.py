# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 00:51:28 2020

@author: HP-MCC
"""
x=0
y=0
path=['U','U','U','D']
for i in path:
    if i=='D':
        x-=1
    else:
        x+=1
    if i=='U' and x==0:
        y+=1
print(y)