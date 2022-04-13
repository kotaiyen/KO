# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 21:20:47 2022

@author: asus
"""

# homework1
for i in range(1,6):
    for j in range(1,i+1):  
      print(i,end='') 
    print()

print()

#homework2
for i in range(5,0,-1):
    for j in range(1,i+1):
        print(i,end='')
    print()

print()

#homework3
for i in range(9,0,-2):
    for j in range(1,i+1):
        print(i,end='')
    print()

print()

#homework4
for i in range(2,101):
    s=0
    for j in range(1,i+1):
        if i%j==0:
            s+=1
    if s==2:
        print (i)
print()   


  
    

    


