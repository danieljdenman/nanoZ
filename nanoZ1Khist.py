# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 10:35:51 2014

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
def nanoZ1KHist(nm, tm=1):

    lft = '/Users/danieljdenman/Academics/allen/BlancheLab/electrodeMeasurements/data/impTesting_23012014/'+nm+'_L_prepost1uADC_500kOhm_target_'+str(1)+'min.txt'
    rgt = '/Users/danieljdenman/Academics/allen/BlancheLab/electrodeMeasurements/data/impTesting_23012014/'+nm+'_R_prepost1uADC_500kOhm_target_'+str(1)+'min.txt'    

    
    #load data
    rL = np.genfromtxt(lft,skip_header=3,skip_footer=1,filling_values = '-1')
    rL = rL[0:rL.shape[0]]
    rR = np.genfromtxt(rgt,skip_header=3,skip_footer=1,filling_values = '-1')
    rR = rR[0:rR.shape[0]]
    numChans = (rL.shape[0])+(rR.shape[0])

    np.ar
    #make a new figure for this electrode
    plt.clf()
    plt.figure(figsize = (7,2))
   
   #analyze phases
    Lphases = rL[:,2];Lphases = Lphases.astype('float')
    Rphases = rR[:,2];Rphases = Rphases.astype('float')
    Lph_hist = np.histogram(Lphases,60,(-100,-40))
    Rph_hist = np.histogram(Rphases,60,(-100,-40))
    allphases = np.concatenate((Lphases,Rphases), axis=0)
    plt.subplot(1,2,1)
    plt.hist(allphases,bins=60,range=(-150,-10),histtype='bar',label=nm)
    plt.axis([-150,-10,0,30])
    
    #analyze Zs
    LZ = rL[:,1];LZ = LZ.astype('float')
    RZ = rR[:,1];RZ = RZ.astype('float')
    LZ_hist = np.histogram(LZ,30,(0,15))
    RZ_hist = np.histogram(RZ,30,(0,15))
    allZs = np.concatenate((LZ,RZ), axis=0)
    plt.subplot(1,2,2)
    plt.hist(allZs,bins=60,range=(0,12),histtype='bar',label=nm)
    plt.axis([0,12,0,30])
    
    plt.show()
    
    lessthan=0
    lessthan4=0
    avgList=[];
    avgList4=[];
    for i in range(0,32):
        if float(rL[i,1]) <= 1:
            lessthan+=1
            avgList.append(rL[i,1])
        if float(rR[i,1]) <= 1:
            lessthan+=1
            avgList.append(rR[i,1])
        if float(rL[i,1]) <= 4:
            lessthan4+=1
            avgList4.append(rL[i,1])
        if float(rR[i,1]) <= 4:
            lessthan4+=1
            avgList4.append(rR[i,1])
    
    ls = np.asarray(avgList)
    print "z<1 : "+str(lessthan)+'   '+str(np.average(ls))+' +/- '+str(np.std(ls))
    ls = np.asarray(avgList4)
    print "z<4 : "+str(lessthan4)+'   '+str(np.average(ls))+' +/- '+str(np.std(ls))
