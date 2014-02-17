# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 16:16:39 2014

@author: danieljdenman
"""
#****************************************************************************
import numpy as np  # NumPy (multidimensional arrays, linear algebra, ...)
import scipy as sp  # SciPy (signal and image processing library)
import os
import matplotlib as mpl         # Matplotlib (2D/3D plotting library)
import matplotlib.pyplot as plt  # Matplotlib's pyplot: MATLAB-like syntax
from pylab import *              # Matplotlib's pylab interface
ion()                            # Turned on Matplotlib's interactive mode
#****************************************************************************

def nanoZ_stabilityFolder(dirname):
    #load all of the .txts from the nanoZ that are in a folder
    [names,allData] = load_nanoZInFolder(dirname)
    
    #try to parse the filenames such that the times can be extracted
    times = np.zeros(len(names),dtype=float); i=0
    for nm in names:
        nm = nm.rstrip('.txt').split('_')
        parsedTime = -1
        for subNM in nm:
            if isinstance(float(subNM.strip('hr')),float):
                parsedTime = float(subNM.strip('hr'))
            else:
                    if isinstance(float(subNM.strip('min')),float):
                        parsedTime = float(subNM.strip('min'))/60
        times[i] = parsedTime        
        i+=1
    
        #show the user the parsing. if it sucks, let the user fix it.
        print times

#function that loads all the nanoZ measurements in a folder.
#returns a list of the names of the txt files.
def load_nanoZInFolder(dirname):
    #make sure there was an input directory, otherwise use a default one
    if not dirname:    
        dirname = '/Users/danieljdenman/Academics/allen/BlancheLab/electrodeMeasurements/imec/data/impTesting_r37_stability/'       

    #go through each file in the folder, open it, determine if it is nanoZ data
        #allow the user to skip, force load, or abort loading altogether
    nms=[]; rL=[]
    for file_name in os.listdir(dirname):
        fullPath = dirname+file_name;
        tmp = np.genfromtxt(fullPath,skip_header=3,skip_footer=1,filling_values = '-1',invalid_raise=False,usecols=(1,2))
        #if no exception (or user forces), put this file in the tuple of open files 
        #and the name of this file in the list of filenames that corresponds to the tuple.        
        if not tmp.any():
            print "------------------------------------------------"            
            print "found a bad one!:  "+fullPath
            print "------------------------------------------------"
        else:
            rL.append(np.genfromtxt(fullPath,skip_header=3,skip_footer=1,filling_values = '-1',invalid_raise=False, usecols=(1,2)))
            nms.append(file_name)

    return [nms,rL]