# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 10:14:41 2014

@author: danield


"""
#****************************************************************************
import numpy as np  # NumPy (multidimensional arrays, linear algebra, ...)
import scipy as sp  # SciPy (signal and image processing library)
import matplotlib as mpl         # Matplotlib (2D/3D plotting library)
import matplotlib.pyplot as plt  # Matplotlib's pyplot: MATLAB-like syntax
from pylab import *              # Matplotlib's pylab interface
ion()                            # Turned on Matplotlib's interactive mode
#****************************************************************************

def zSpectrum(nm):
#djd    
    #load data
    rNM='/Users/danieljdenman/Academics/allen/BlancheLab/electrodeMeasurements/data/'+nm+'_spectroscopy_L.txt'
    lNM='/Users/danieljdenman/Academics/allen/BlancheLab/electrodeMeasurements/data/'+nm+'_spectroscopy_R.txt'    
    r6Ls = np.loadtxt(lNM,dtype='str',skiprows=2)
    r6Ls = r6Ls[0:r6Ls.shape[0]-1]
    r6Rs = np.loadtxt(rNM,dtype='str',skiprows=2)
    r6Rs = r6Rs[0:r6Rs.shape[0]-1]
    freq = [1,2,5,10,20,50,100,200,500,1000,2000]
    numchans = r6Ls.shape[0]+r6Rs.shape[0]
    
    #instantiate avg lists
    avgZ = [] #np.zeros(len(freq)); numGood = 0
    
    plt.clf()
    
    #create separate Z and phase arrays
    #zIndices = (np.array(range(0,11))*2)+1
    #pIndices = (np.array(range(0,11))*2)+2
    r6Lz=np.zeros((numchans/2,len(freq)));r6LP=np.zeros((numchans/2,len(freq)))
    r6Rz=np.zeros((numchans/2,len(freq)));r6RP=np.zeros((numchans/2,len(freq)))
    for i in range(0,numchans/2):
        for j in range(0,11):
            r6Lz[i,j]=r6Ls[i][j*2+1]
            r6LP[i,j]=r6Ls[i][j*2+2]
            r6Rz[i,j]=r6Rs[i][j*2+1]
            r6RP[i,j]=r6Rs[i][j*2+2]
            
    #plot all z
    plt.subplot(1,2,1)
    for i in range(0,r6Lz.shape[0]):
        if r6Lz[i,9]<4:
            plt.plot(freq,r6Lz[i,:])
            avgZ.append(r6Lz[i,:]);avgP.append(r6LP[i,:])
        if r6Rz[i,9]<4:
            plt.plot(freq,r6Rz[i,:])
            avgZ.append(r6Rz[i,:]);avgP.append(r6RP[i,:])
    plt.xscale('log');plt.yscale('log')
    plt.axis([0.9,2100,0.1,5000])
    
    #plot the avg z
    zArray = np.array(avgZ);
    avZ=np.mean(zArray,axis=0) 
    sdZ=np.std(zArray,axis=0)
    plt.subplot(1,2,2)
    plt.errorbar(freq,avZ,yerr=sdZ)
    plt.xscale('log');plt.yscale('log')
    plt.axis([0.9,2100,0.1,5000])
    
    plt.show()
      

#plot phase
#z = plot()
#for i in range(0,r6LP.shape[0]):
#    plt.plot(freq,r6LP[i,:])
#    plt.plot(freq,r6RP[i,:])
#plt.axis([0.9,2000,-150,150])
#plt.xscale('log')
#plt.show()
#