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

def nanoZ_plotLongitudinal(dirname):

    [times,names,means,stds,sems,medians,allData] = nanoZ_stabilityFolder(dirname)

    plt.clf()
    plt.figure(figsize = (7,2))
    plt.errorbar(times,means,yerr=sems,linestyle='')
    plt.xscale('log');
    plt.axis([0.01,2.1,0.23,0.265])


def nanoZ_stabilityFolder(dirname):
    #load all of the .txts from the nanoZ that are in a folder
    [names,allData] = load_nanoZInFolder(dirname)
    
    #try to parse the filenames such that the times can be extracted
    times = np.zeros(len(names),dtype=float);
    for i in range(0,len(names)):
        nm = names[i].rstrip('.txt').split('_')
        parsedTime = -1
        for subNM in nm:
            if subNM.strip('hr').isdigit():
                parsedTime = float(subNM.strip('hr'))
            else:
                    if subNM.strip('min').isdigit():
                        parsedTime = float(subNM.strip('min'))/60
        times[i] = parsedTime        
    
    #show the user the parsing. if it sucks, let the user fix it.<-- not implemented. TODO
    
    #ask the user about the probe, to know which channels to ignore
    #maskDictionary contains properly masked channels for certain configureation of 
    #the nanoZ. ask Dan for more details.
    maskDictionary = {'imec_right':[0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1],
                      'imec_left':[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,1,0,1,0,0],
                        'imec_right2':[0,0,1,0,0,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
                      'imec_left2':[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,1,0,1,0,0],
}
    #maskDictionary.setdefault([0]*len(allData[0][:,0]))#np.zeros(len(allData[0][:,0])))  
           
    probe=raw_input('tell me about the probe. your options are: imec_left, imec_right: ')    
    mask = maskDictionary[probe]

    #proceed only if the data and mask are alignabled    
    if len(mask)==len(allData[0][:,0]):
        #go through and remove the channels known to be open        
        for i in range(0,len(mask)-1):
            if mask[31-i]==1:
                for j in range(0,len(times)):
                    allData[j]=np.delete(allData[j],31-i,0); #this is where open channels are deleted
    else:
        print 'mask:'+str(len(mask))+' and data:'+str(len(allData[0][:,0]))+' do not match\rcheck the loader to see how many lines it skipped.'

        
    #make oneD arrays that match time
    means = np.zeros(len(times))
    stds = np.zeros(len(times))
    sems = np.zeros(len(times))
    medians = np.zeros(len(times))
    for i in range(0,len(times)):
        means[i] = np.mean(allData[i][:,0])
        stds[i] = np.std(allData[i][:,0])
        sems[i] = stds[i]/np.sqrt(len(allData[i][:,0]))
        medians = np.median(allData[i][:,0])
    
    #return the results    
    return [times,names,means,stds,sems,medians,allData]


#make distribution of Z @ 1K
def nanoZ1KHist(nm, tm=1):

    lft = '/Users/danieljdenman/Academics/allen/BlancheLab/electrodeMeasurements/imec/20140213/D22/D22_1K_L_'+nm+'min.txt'
    rgt = '/Users/danieljdenman/Academics/allen/BlancheLab/electrodeMeasurements/imec/20140213/D22/D22_1K_R_'+nm+'min.txt' 

    
    #load data
    rL = np.genfromtxt(lft,skip_header=3,skip_footer=1,filling_values = '-1')
    rL = rL[0:rL.shape[0]]
    rR = np.genfromtxt(rgt,skip_header=3,skip_footer=1,filling_values = '-1')
    rR = rR[0:rR.shape[0]]
    numChans = (rL.shape[0])+(rR.shape[0])

   # np.ar
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
    plt.hist(allphases,bins=40,range=(-100,-10),histtype='bar',label=nm)
    plt.axis([-100,-10,0,20])
    
    #analyze Zs
    LZ = rL[:,1];LZ = LZ.astype('float')
    RZ = rR[:,1];RZ = RZ.astype('float')
    LZ_hist = np.histogram(LZ,30,(0,15))
    RZ_hist = np.histogram(RZ,30,(0,15))
    allZs = np.concatenate((LZ,RZ), axis=0)
    plt.subplot(1,2,2)
    plt.hist(allZs,bins=40,range=(0,1),histtype='bar',label=nm)
    plt.axis([0,1,0,20])
    
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
    
#______________________________________________________________________________
#--------------------------tools used in above scripts--------------------------
#______________________________________________________________________________

#******************************************************************************
def load_nanoZInFolder(dirname):
#function that loads all the nanoZ measurements in a folder.
#returns a list of the names of the txt files.

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
#******************************************************************************
#******************************************************************************
def dSimpleStats(inpt):
#function that returns the mean, st. dev., and s.e.m., median of an array of numbers
#returns: [mean,s.d.,s.e.m.,median]
    mn = np.mean(inpt)
    sd = np.std(inpt)
    sem = sd/np.sqrt(len(inpt))
    md = np.median(inpt)
    return [mn,sd,sem,md]
#******************************************************************************