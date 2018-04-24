#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 14:11:06 2018

@author: alwin
"""

import random
import sys
import os

super_villains = {'Fiddler' : 'Issac Bowin', 
                  'Captain Cold' : 'Leonard Snart',
                  'Weather Wizard' : 'Mark Marden', 
                  'Mirror Master' : 'Sam Scudder', 
                  'Pied Piper' : 'Thomas Peterson' }

print(super_villains)
print()
print(super_villains['Captain Cold'])
print()
del super_villains['Fiddler']
print(super_villains)
super_villains['Pied Piper'] = 'Hartley Rathway'
print()
print(super_villains)
print()
print(len(super_villains))
print()
print(super_villains.get("Mirror Master"))
print()
print(super_villains.keys())
print()
print(super_villains.values())