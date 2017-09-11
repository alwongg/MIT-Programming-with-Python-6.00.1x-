#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 23:26:02 2017

@author: alex
"""

# Problem 1

# Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'

s = input("Enter a string: ")
vowel = 0
for letter in s:
    if letter in 'aeiou':
        vowel += 1
print("Number of vowels: " + str(vowel))
        
        
        
        


