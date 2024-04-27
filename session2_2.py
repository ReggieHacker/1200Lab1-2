#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 21:28:41 2024

@author: reggiehacker
"""

##Ball Problem
#Gather user input for the velocity of the ball in meters per second
print('Velocity of ball: ')
v = float(input())

#calculate the position of the ball
s = (v**2)/19.6

print(str(s) + ' meters')

