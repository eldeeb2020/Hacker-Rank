# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 02:16:34 2020

@author: Ahmed Omar
"""
ar=[1,3,2,6,1,2]
k=3
n=0
arr=[]
for i  in range(len(ar)):
    for j in range (len(ar)):
        if i<j and (ar[i]+ar[j])%k==0:
            n+=1
            
print(n)
print(arr)

