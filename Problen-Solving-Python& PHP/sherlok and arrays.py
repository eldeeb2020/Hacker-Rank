# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 00:13:52 2020

@author: Ahmed Omar
"""
ar=[0,9,8,1]
n=0
def fun(ar):
    for i in range (0,len(ar)):
        if sum(ar[0:i])==sum(ar[i+1:len(ar)+1]):
            return ("YES")
        #break
    return "NO"
#if n==1:
 #   print("YES")
#else:
 #   print("NO")
 
x=fun(ar)
print(x)
#######################################################33
#faster implementation after optimization

def fun(ar):
    s=sum(ar)
    l=0
    for i in ar:
        if l==s-i-l:
            return "YES"
        l+=i
    return "NO"
        
       

