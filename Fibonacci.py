# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 20:59:25 2018

@author: Ade Teriba
"""

def fib(x):
    x = input('Enter a number: ')
    if(int(x)==0):
        return 0
    elif (int(x)==1):
        return 1
    else:
        return fib(x-1)+fib(x-2) 
    print(fib(x))

