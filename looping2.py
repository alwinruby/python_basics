#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 21:06:34 2018

@author: alwin
"""

import random

random_num = random.randrange(0, 100)

while(random_num != 15):
    print(random_num)
    random_num = random.randrange(0, 100)