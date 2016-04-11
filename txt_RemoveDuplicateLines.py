# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 16:50:27 2016

@author: ee10sjo
"""


import os

dir = os.getcwd()

f_in = open('MostWellData.txt')
f_out = open('MostWellData_noDuplicates.txt', 'w')
unique = []

for line in f_in:
    if line not in unique:
        f_out.write(line)
        unique.append(line)
f_out.close()
f_in.close()
