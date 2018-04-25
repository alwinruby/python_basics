#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 10:03:09 2018

@author: alwin
"""

age = 19

if age > 17:
    print("You are old enough to drive")
    print()
else :
    print("You are not old enough to drive")
    print()

if age >= 21:
    print("You are old enough to drive a tractor trailer")
    print()
elif age >= 17:
    print("You are not old enough to drive a car")
    print()
else :
    print("You are not old enough to drive")
    print()


if ((age >= 1)and (age <= 18)):
    print("You get a birthday")
    print()
elif ((age == 21) or (age >= 65)):
    print("You also get a birthday")
    print()
elif not(age == 20):
    print("You DON'T get a birthday")
    print()
else :
    print("You get a birthday PARTY!!!! YEAH!")
    print()