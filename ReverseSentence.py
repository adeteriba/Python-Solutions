# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 19:14:52 2018

@author: Ade Teriba
"""
#print the sentence backwards
str = input('Enter a sentence: ')
x = str.split()
str_rev = ' '.join(reversed(x))
print(str_rev)  
