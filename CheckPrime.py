# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 16:18:09 2018

@author: Ade Teriba
"""

x = input('Enter a number: ') #Asking the user to enter a number to be checked

def check(x):
    if int(x) > 1: #Prime numbers are greater than 1
        for i in range(2,int(x)):
            if (int(x)%2)==0:
                print(x,'is not a prime number')
                break
            else:
                print(x,'is a prime number')
                break
        return ' '
print(check(x))
            
            
    

        