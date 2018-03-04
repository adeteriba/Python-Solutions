# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 23:16:32 2018

@author: Ade Teriba
"""

x = input('Enter a number: ')
def weather(x):
    if(int(x)>=0 and int(x)<=8):
        print('It is cold outside, bring a jacket!')
    elif(int(x)>=9 and int(x)<=16):
        print("The sun is coming out, and it is getting warmer")
    elif(int(x)>=17 and int(x)<=32):
        print('Time to sit beside the pool and relax')
    elif(int(x)>=33 and int(x)<=45):
        print('Too hot, cant move')
    if(int(x)<0 or int(x)>45):
        print('Not a valid number!')
        return ' '
        
print(weather(x))
    
