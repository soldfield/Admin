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


def remove_op(fn, operator = '.', extn = '.txt'):
    """
    Remove operator from file names and add an extension
    """
    fn.split('.')
    return fn


def remove_operator(path, operator='.'):
    fl = os.listdir(path)
    for i in range(len(fl)):
        fn_in = fl[i]
        fp_in = path + fn_in
        fn_out = fn_in.split(operator)
        fn_out = '_'.join(fn_out)
        fp_out = path + fn_out

        os.rename(fp_in, fp_out)

#remove_operator(path, '-')


path = "C:\\Users\\ee10sjo\\Documents\\BaseCaseSurfaces\\"

os.chdir(path)

