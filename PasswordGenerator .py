# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 11:25:12 2018

@author: Ade Teriba
"""
import random

characters = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
password_size = 8
#The method join() returns a string in which the string elements of sequence have been joined by str separator.
password = "".join(random.sample(characters,password_size))
print("Your password is",password)

