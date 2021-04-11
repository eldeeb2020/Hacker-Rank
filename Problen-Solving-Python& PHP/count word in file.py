# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 23:50:07 2020

@author: Ahmed Omar
"""


file=open('ahmed&mohamed.txt','r')
dic=dict()
for word in file:
    x=word.split()#conver each line to list of word for all words in this line
    x.sort()
    print(x)
    for i in x:
        dic[i]=dic.get(i,0)+1 
    print(dic)
    dic.clear()
############################################################
#another method
file=open('ahmed&mohamed.txt','r')
lst=[]
for word in file:
    x=word.split()
    x.sort()
    while len(x)>0:
        z=x.count(x[0])
        lst.append(x[0])
        lst.append(z)
        for i in range(0,z):
            x.remove(x[0])
    print(lst)

        


    

