# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 15:15:55 2016

Script to extract location data from a set of las files and produce a summary
table.

@author: Simon J Oldfield


   Copyright 2015 Simon J. Oldfield

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
   
   
"""



# MVP - Script that extracts location data from a series of las files
# result shoudl be assembled ina form that can later be manipulated
# in a spreadsheet.

import os
import glob
import lasio


# identify las files in directory
dir = os.getcwd()
las_ls = glob.glob("*.las")

for i in las_ls:
    lasio.read(i)


# from lasio header extract, pull well name, field name, UWI, LATI, LONG

DesHdrs = ("UWI", "WELL-NAME", "FIELD-NAME", "LONG", "LATI")

# Loop list of desired headers to build database
for i in DesHdrs:
    l.well[i].value


#return d