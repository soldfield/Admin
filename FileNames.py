# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 09:36:46 2016

Various functions for basic administrative tasks.

@author: ee10sjo
"""

from os import listdir
import os

def extn_add(dir, extn):
    """
    Function to add a file extension to all files within a provided directory.
    """

    for f in listdir(dir):
        new_fn = os.path.join(dir, f + extn)
        old_fn = os.path.join(dir, f)
        os.rename(old_fn, new_fn)
        
    result = listdir(dir)
    print(result)

