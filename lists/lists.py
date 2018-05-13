#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 12:12:13 2018

@author: alwin
"""

import random
import sys
import os


grocery_list = ['Juice', 'Leeks', 'Potatoes', 'Bananas']

print('First Item:', grocery_list[0])
print()
print(grocery_list[1:3])
other_events = ['Wash Car', 'Pick up kids', 'Car check']

to_do_list = [other_events, grocery_list]
print()
print(to_do_list)
print()
print((to_do_list[1][1]))
grocery_list.append('Onions')
print()
print(to_do_list)
print()
grocery_list.insert(1, 'Pickle')
print()
print(to_do_list)
print()
grocery_list.remove('Pickle')
print()
print(to_do_list)
print()
grocery_list.sort()
print()
print(to_do_list)
print()
grocery_list.reverse()
print()
print(to_do_list)
print()
to_do_list2 = other_events + grocery_list
print(to_do_list2)