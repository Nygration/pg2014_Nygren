# -*- coding: utf-8 -*-
"""
Created on Tue Dec 09 15:34:33 2014
@author:Chris Nygren
Making a netCDF file from the wave class we made
We'll run it forward and save every few time steps to the netCDF file

"""
import numpy as np
import matplotlib.pyplot as plt
import netCDF4

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
        
    def makenet(self,name1='temp',steps=100,save_every=1):
        nc=netCDF4.Dataset('%s.nc' % name1,'w',clobber=True)
        nc.createDimension('x', len(self.eta))
        nc.createDimension('time', None)

        nc.createVariable('eta','d',('time','x'))
        nc.variables['eta'].units='meters'
        nc.createVariable('time','d',('time',))
        nc.variables['time'].units='seconds'        
        
        self.step(steps) #move forward in time
        indexes=np.arange(0,steps,save_every)#get the indexes of the data you want saved
        nc.variables['time'][:]=indexes
        nc.variables['eta'][:]=self.etachange[indexes]
        
        nc.close()
        
if __name__ =='__main__':        
    initial=np.array([1.0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1.0])
    basin1=slosh(initial)
    basin1.makenet('everyten',steps=101,save_every=10)
    netbasin1=netCDF4.Dataset('everyten.nc')
    print 'the variable keys are:', netbasin1.variables.keys()
    print 'the length of the basin is %d' % len(initial)
    print 'the number of steps taken was %d, but the inital state was also stored' % int(101.0/10.0)
    print 'the shape of eta is:', np.shape(netbasin1.variables['eta'][:])
        