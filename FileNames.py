# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 09:36:46 2016





@author: ee10sjo
"""



from os import listdir
from os.path import join
import os

dir_name = "Y:\\ee10sjo\\Oldfields_PhD\\4_Applications\\Python\\SurfaceAttributeAnalysis\\AttributeGrids\\"

listdir(dir_name)[0:17]

extn = ".zmap"

for i in listdir(dir_name)[0:17]:
    newfn = os.path.join(dir_name, i + extn)
    
    old = dir_name + i
    os.rename()
    
result = listdir(dir_name)
print(result)

