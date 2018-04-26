#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 21:06:34 2018

@author: alwin
"""

for x in range(0, 10):
    print(x, ' ', end=" ")
print('\n')

grocery_list = ['Juice', 'Tomatoes', 'Potatoes', 'Bananas']

for y in grocery_list:
    print(y)
    
print('\n')
   
for x in [2,4,6,8,10]:
    print(x)
    
num_list = [[1, 2, 3], [10, 20, 30], [110, 220, 330]]

for x in range(0, 3):
    for y in range(0, 3):
        print(num_list[x][y])