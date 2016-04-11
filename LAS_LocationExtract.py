# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 15:15:55 2016

Script to extract location data from a set of las files and produce a summary
table.

@author: Simon J Oldfield

"""

# MVP - Script that extracts location data from a series of las files
# result should be assembled in a form that can later be manipulated
# in a spreadsheet.

import os
import glob
import lasio


# identify las files in directory
dir = 'Y:\\ee10sjo\\Oldfields_PhD\\3_Data\\ECO_Data_07Sep2015\\Wells_LASLogs_Selected_SO'
os.chdir(dir)
las_ls = glob.glob("*.las")

def las_hdr_extract(las_ls):
    #Open file for storing results.  
    f = open('./test', 'w')
    
    # Loop through header extraction.
    for i in range(len(las_ls)):
        d = lasio.read(las_ls[i])
        uwi = d.well["UWI"].value
        wlnam = d.well["WELL-NAME"].value
        fldnam = d.well["FIELD-NAME"].value
        long = str(d.well["LONG"].value)
        lati = str(d.well["LATI"].value)
        output = uwi + ', ' + str(wlnam) + ', ' + str(fldnam) + ', ' +  str(long) + ', ' +  str(lati) + '\n'
        try:
            f.write(output)
        except:
            print(las_ls[i])
            continue
        
        #return uwi, wlnam, fldnam, long, lati # Legacy code
        
    # close file leaving it ready for use
    f.close()

