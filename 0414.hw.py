# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 22:08:57 2022

@author: asus
"""


#hw1

import random

number = random.randint(1,100)

guess = -1

start = 1 

end = 100

while True :
    guess = int (input("請輸入{}~{}之間的數:".format(start,end)))
    if guess == number:
        print("猜對了!，數字是:",number)
        break
    elif guess > number:
        end = guess
        print("{}~{}之間".format(start,end))
    elif guess < number:
        start = guess
        print("{}~{}之間".format(start,end))
      
print("程式執行完畢")

















