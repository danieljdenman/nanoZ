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
def nanoZ1KHist(nm):
    lft = '/Users/danieljdenman/Desktop/R'+nm+'_1K_L.txt'
    rgt = '/Users/danieljdenman/Desktop/R'+nm+'_1K_R.txt'
    
    #load data
    r6L = np.loadtxt(rgt,dtype='str',skiprows=2)
    r6L = r6L[0:r6L.shape[0]-1]
    r6R = np.loadtxt(lft,dtype='str',skiprows=2)
    r6R = r6R[0:r6R.shape[0]-1]
    numChans = (r6L.shape[0]-1)+(r6R.shape[0]-1)
    
    #analyze phases
    Lphases = r6L[:,2];Lphases = Lphases.astype('float')
    Rphases = r6R[:,2];Rphases = Rphases.astype('float')
    Lph_hist = np.histogram(Lphases,60,(-100,-40))
    Rph_hist = np.histogram(Rphases,60,(-100,-40))
    allphases = np.concatenate((Lphases,Rphases), axis=0)
    plt.subplot(1,2,1)
    plt.hist(allphases,bins=30,range=(-150,-10),histtype='bar')
    plt.axis([-150,-10,0,25])
    
    #analyze Zs
    LZ = r6L[:,1];LZ = LZ.astype('float')
    RZ = r6R[:,1];RZ = RZ.astype('float')
    LZ_hist = np.histogram(LZ,30,(0,15))
    RZ_hist = np.histogram(RZ,30,(0,15))
    allZs = np.concatenate((LZ,RZ), axis=0)
    plt.subplot(1,2,2)
    plt.hist(allZs,bins=30,range=(0,15),histtype='bar')
    plt.axis([0,15,0,25])
    
    #plt.hist(RZ,bins=120,range=(0,30),histtype='bar')