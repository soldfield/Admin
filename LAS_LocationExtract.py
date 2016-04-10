# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 15:15:55 2016

Script to extract location data from a set of las files and produce a summary
table.

@author: Simon J Oldfield

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

def las_hdr_extract(las_ls):
    for i in range(len(las_ls)):
        d = lasio.read(las_ls[0])
        uwi = d.well["UWI"].value
        wlnam = d.well["WELL-NAME"].value
        fldnam = d.well["FIELD-NAME"].value
        long = str(d.well["LONG"].value)
        lati = str(d.well["LATI"].value)
        print(uwi + ', ' + wlnam + ', ' + fldnam  + ', ' +  long  + ', ' +  lati)


f1=open('./testfile', 'w+')
f1.write(las_hdr_extract(las_ls))
f1.close()