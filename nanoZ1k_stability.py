# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 09:19:51 2014

@author: danieljdenman
"""

#****************************************************************************
import numpy as np  # NumPy (multidimensional arrays, linear algebra, ...)
import scipy as sp  # SciPy (signal and image processing library)
import matplotlib as mpl         # Matplotlib (2D/3D plotting library)
import matplotlib.pyplot as plt  # Matplotlib's pyplot: MATLAB-like syntax
from pylab import *              # Matplotlib's pylab interface
ion()                            # Turned on Matplotlib's interactive mode
#****************************************************************************

#make distribution of Z @ 1K
def nanoZ1K_stability(nm):

    #load the data
    lftP =  '/Users/danieljdenman/Academics/allen/BlancheLab/electrodeMeasurements/data/impTesting_23012014/'+nm+'_L_1K.txt'
    rgtP =  '/Users/danieljdenman/Academics/allen/BlancheLab/electrodeMeasurements/data/impTesting_23012014/'+nm+'_R_1K.txt'
    #lft =  '/Users/danieljdenman/Academics/allen/BlancheLab/electrodeMeasurements/data/impTesting_23012014/'+nm+'_L_prepost1uADC_500kOhm_target.txt'
    #rgt =  '/Users/danieljdenman/Academics/allen/BlancheLab/electrodeMeasurements/data/impTesting_23012014/'+nm+'_R_prepost1uADC_500kOhm_target.txt'
    lft1 = '/Users/danieljdenman/Academics/allen/BlancheLab/electrodeMeasurements/data/impTesting_23012014/'+nm+'_L_prepost1uADC_500kOhm_target_1min.txt'
    rgt1 = '/Users/danieljdenman/Academics/allen/BlancheLab/electrodeMeasurements/data/impTesting_23012014/'+nm+'_R_prepost1uADC_500kOhm_target_1min.txt'    
    lft5 = '/Users/danieljdenman/Academics/allen/BlancheLab/electrodeMeasurements/data/impTesting_23012014/'+nm+'_L_prepost1uADC_500kOhm_target_5min.txt'
    rgt5 = '/Users/danieljdenman/Academics/allen/BlancheLab/electrodeMeasurements/data/impTesting_23012014/'+nm+'_R_prepost1uADC_500kOhm_target_5min.txt'    
    lft10 = '/Users/danieljdenman/Academics/allen/BlancheLab/electrodeMeasurements/data/impTesting_23012014/'+nm+'_L_prepost1uADC_500kOhm_target_10min.txt'
    rgt10 = '/Users/danieljdenman/Academics/allen/BlancheLab/electrodeMeasurements/data/impTesting_23012014/'+nm+'_R_prepost1uADC_500kOhm_target_10min.txt'    
    lft20 = '/Users/danieljdenman/Academics/allen/BlancheLab/electrodeMeasurements/data/impTesting_23012014/'+nm+'_L_prepost1uADC_500kOhm_target_20min.txt'
    rgt20 = '/Users/danieljdenman/Academics/allen/BlancheLab/electrodeMeasurements/data/impTesting_23012014/'+nm+'_R_prepost1uADC_500kOhm_target_20min.txt'    
    pre = np.concatenate((np.genfromtxt(lftP,skip_header=3,skip_footer=1,filling_values = '-1'),np.genfromtxt(rgtP,skip_header=3,skip_footer=1,filling_values = '-1')))
    #dc = np.concatenate((np.genfromtxt(lft,skip_header=3,skip_footer=1,filling_values = '-1'),np.genfromtxt(rgt,skip_header=3,skip_footer=1,filling_values = '-1')))
    #one = np.concatenate((np.genfromtxt(lft1,skip_header=3,skip_footer=1,filling_values = '-1'),np.genfromtxt(rgt1,skip_header=3,skip_footer=1,filling_values = '-1')))
    #five = np.concatenate((np.genfromtxt(lft5,skip_header=3,skip_footer=1,filling_values = '-1'),np.genfromtxt(rgt5,skip_header=3,skip_footer=1,filling_values = '-1')))
    #ten = np.concatenate((np.genfromtxt(lft10,skip_header=3,skip_footer=1,filling_values = '-1'),np.genfromtxt(rgt10,skip_header=3,skip_footer=1,filling_values = '-1')))
    twenty = np.concatenate((np.genfromtxt(lft20,skip_header=3,skip_footer=1,filling_values = '-1'),np.genfromtxt(rgt20,skip_header=3,skip_footer=1,filling_values = '-1')))
            
    #renumber the second set as 33-64
    for i in range(0,pre.shape[0]):
        if i>31:
            pre[i,0]=i+1;
            #dc[i,0]=i+1;
            #one[i,0]=i+1;
            #five[i,0]=i+1;
            #ten[i,0]=i+1;
            twenty[i,0]=i+1

        plt.clf()
        plt.figure(figsize=(7,2))
        
    #plot Z as a function of channel number
        plt.plot(pre[:,0],pre[:,1],'wo')
        #plt.plot(one[:,0],one[:,1],'o')
        #plt.plot(five[:,0],five[:,1],'o')
        #plt.plot(ten[:,0],ten[:,1],'o')
        plt.plot(twenty[:,0],twenty[:,1],'ko')
        plt.plot()
        plt.yscale('log');plt.axis([0,65,0.1,12])