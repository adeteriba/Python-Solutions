# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 23:56:06 2018

@author: Ade Teriba
"""
x = input('Enter a number: ')
def star(x):
    for i in range(1,int(x)): #the fange function was used to count from 1 to not including the inutted number
        print('*' * i)  #The string is multiplied by the numberand print '*' x times
print(star(x))