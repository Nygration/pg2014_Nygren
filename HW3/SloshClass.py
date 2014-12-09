# -*- coding: utf-8 -*-
"""
Created on Thu Nov 06 14:04:29 2014

@author: User
"""
import numpy as np
import matplotlib.pyplot as plt
######################
def Checker(a,b,n,x):
    """n should be the index of the last element in the arrays being compared(a and b)
    So n should be =len(a)-1 == len(b)-1
    Also x is the minimum change requirement, for stoessels class he wants .05 mm so x==.0005
    this function returns true if the differences between a and b are larger than x and false if they are not
    presummably a is the initial condition and b is the next time step so this check to see if the changes are small enough to stop looping through time steps
    """
    if n==0:
        if abs(a[0]-b[0])>=x: #if the changes in eta from one time step to another is more than .05mm
            return True            #return true to continue the loop
        else:
            return False            #stop the loop (this only happens if all of the points had a change of less than .05mm)
    elif abs(a[n]-b[n])>=x:    #this checks each of the points in the channel 
        return True                 #if any have too big a change the loop continues
    else:                           #if that point in the channel has small enough change
        Checker(a,b,n-1)            #check the next point in the channel
#########################
class slosh(object):
    """ This class will take in an array for eta that will be the starting SSH, it will also take the depth (H)[flat bottom]
    as well as the spatial and time steps dx and dt and how many itterations to run.
    It will out put a graph showing ssh and velocity. This may be changed later   
    Make sure you meet the CFL criteria (have dx much bigger than dt else it looks like crap)
    """
    
    def __init__(self,eta,H0=10.0,dx=100.0,dt=5.0):    
        self.length=len(eta)                     #length of the given eta (allows program to take eta of any length)
        self.uuu=np.array(np.zeros(self.length+1))    #current velocities (start at rest)
        self.uuuF=np.array(np.zeros(self.length+1))   #future velocities
        self.etaF=np.array(np.zeros(self.length))     #Future ssh
        self.g=9.81 #gravty (m/s²)
        self.uuuchange=np.array(np.zeros(self.length+1)) #these will track changes
        self.etachange=eta   #this will track changes and is initialized with the starting state
        self.eta=eta        
        self.H0=H0
        self.dx=dx
        self.dt=dt
    
    def step(self,n):
        for t in range(n):
            self.uuuF[0]=0
            self.uuuF[-1]=0
            self.uuuF[1:-1]=self.uuu[1:-1]-(self.g*self.dt/self.dx)*(self.eta[1:]-self.eta[:-1]) #calculate the new values
            self.etaF=self.eta-(self.H0*self.dt/self.dx)*(self.uuuF[1:]-self.uuuF[:-1])            #calculate the new values
            self.uuuchange=np.vstack([self.uuuchange,self.uuuF])           #track the changes
            self.etachange=np.vstack([self.etachange,self.etaF])           #track the changes
            self.uuu=self.uuuF    #reset to new values for the next itteration
            self.eta=self.etaF    #reset to new valuse for the next itteration

    def checkstep(self):
        print len(self.etachange)
        
    def pull(self,index):
        return self.etachange[index]
        
    def color(self):
        figure1=plt.figure(figsize=(12,8)) # make the figure
        ax1=figure1.add_subplot(121)
        ax2=figure1.add_subplot(122)    
        ax1.set_title('Velocity [m/s]') #label subplot 1
        ax1.set_xlabel('Point in the channel (%fm apart)' %(self.dx))
        ax2.set_title('SSH anomaly [m]') #label subplot 2
        ax2.set_xlabel('Point in the channel (%fm apart)' %(self.dx))
        #This bit is for the Pcolors
        #"""
        ax1.set_xlim(0,self.length+1)
        #ax1.set_ylim(n,0)  
        ax1.set_ylabel('Time Step (%f seconds)' %(self.dt))
        ax2.set_xlim(0,self.length)
        #ax2.set_ylim(n,0)    
        ax2.set_ylabel('Time Step (%f seconds)' %(self.dt))
        uuupc=ax1.pcolor(self.uuuchange, cmap=plt.cm.RdBu_r)
        uuucb=plt.colorbar(self.uuupc, ax=ax1, orientation='horizontal')
        etapc=ax2.pcolor(self.etachange, cmap=plt.cm.RdBu_r)
        etacb=plt.colorbar(self.etapc, ax=ax2, orientation='horizontal')
        #"""
        figure1.show()    
    
    def line(self):
        figure1=plt.figure(figsize=(12,8)) # make the figure
        ax1=figure1.add_subplot(121)
        ax2=figure1.add_subplot(122)    
        ax1.set_title('Velocity [m/s]') #label subplot 1
        ax1.set_xlabel('Point in the channel (%fm apart)' %(self.dx))
        ax2.set_title('SSH anomaly [m]') #label subplot 2
        ax2.set_xlabel('Point in the channel (%fm apart)' %(self.dx))
        #this bit is for lineplots
        #"""
        uuuplt=ax1.plot(self.uuu)
        etaplt=ax2.plot(self.eta)
        ax1.set_xlim(0,self.length)
        ax1.set_ylabel('Velocity [m/s]')
        ax2.set_xlim(0,self.length-1)
        ax2.set_ylabel('SSH anomaly [m]')
        #"""    
        figure1.show()

    
    
initial=np.array([1.0,0,0,0,0,0,0,0,0,0,0,0,0,1.0])
basin1=slosh(initial)
basin1.step(100)

plt.plot(basin1.pull(0))
plt.show()

