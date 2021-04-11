# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 19:04:45 2020

@author: Ahmed Omar
"""
a=[2,4]
b=[16,32,96]
a.sort()
b.sort()
k=0
z=0
d=0
f=0
x=[]
y=[]
n=a[-1]
r=0
while n<=b[0]:
    for i in a:
        k=n%i
        z=z+k
    if z==0:
        y.append(n)
    n+=a[-1]
    z=0
    k=0
print(y)

for i in y:
    for j in b:
        d=j%i
        f=d+f
    if f==0:
        r=r+1
        f=0
        d=0
print (r)
        
        
            
    
    

    