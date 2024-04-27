#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 21:28:42 2024

@author: reggiehacker
"""

##Box Problem
import numpy as np

#Gather user input for the mass of the box in kilograms
print('What is the mass of the box in kg: ')
m = float(input())

#Gather user input for coefficient of kinetic friction
print('What is the coefficient of kinetic friction: ')
uk = float(input())

#gather user input for the angle of the slope the box is on in radians
print('What is the angle of the slope in radians: ')
rad = float(input())

#calculate the force in Newtons
f = float(np.cos(rad) * m * 9.8 * uk)

#print calculation
print(str(f) + ' N')

