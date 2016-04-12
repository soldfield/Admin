# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 13:46:46 2016

@author: ee10sjo
"""



import os
import pandas as pd
import numpy as np

os.chdir('Y:\\ee10sjo\\Oldfields_PhD\\3_Data\\ECO_Data_07Sep2015\\Wells')


xls = pd.ExcelFile("MergedWellLists.xlsx")
df1 = xls.parse("MostWellData_noDuplicates")
df2 = xls.parse("Well Data GIS")


