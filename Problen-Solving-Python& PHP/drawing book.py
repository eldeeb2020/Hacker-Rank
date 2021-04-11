# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 19:45:34 2020

@author: Ahmed Omar
"""
n=6
p=5
y=0
if (p<=n//2):
    x=p//2
elif (p==n):
    x=0
elif (p==n-1 and n%2==0 ):
    x=1
    
else:
    while p<n:
        y+=1
        p+=1
    x=y//2
print(x)
    

