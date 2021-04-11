# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 18:56:11 2020

@author: Ahmed Omar
"""
keyboards=[6,6,6]
drives=[1,2,3,4]
b=6
lst=[]
for i in keyboards:
   for j in drives:
       if i+j<=b:
           lst.append(i+j)
if lst==[]:
    print (-1)
else:
    print (max(lst))

