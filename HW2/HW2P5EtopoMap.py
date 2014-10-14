# -*- coding: utf-8 -*-
"""
Created on Tue Oct 14 02:14:59 2014
@author: Chris Nygren
HW2P5 Write a function to read the topography/bathymetry of the world using the ETOPO5 surface dataset:

http://www.nio.org/userfiles/file/datainfo/global_merged5.txt

and return three arrays representing x, y, and z. Write a script using this function to make
a pcolormesh map of the topo/bathy, and overlay the contours z = [-1000, 0, 1000]. The
negative contour should be thin and dashed, the 0 contour thick and solid, and the 1000
contour thin and solid.
"""

import matplotlib.pyplot as plt
import numpy as np

dataurl='http://www.nio.org/userfiles/file/datainfo/global_merged5'
datafilename='global_merged5.txt' # get the file name

dataraw=np.loadtxt(datafilename) # read in the data, leave as floats
Lon=dataraw[:,0] #get the lon data
Lat=dataraw[:,1] #get the lat data
Top=dataraw[:,2] #get the topography data


XXX=Lon.reshape(2161,4321) #makes a nice grid array so we don't need meshgrid
YYY=Lat.reshape(2161,4321) #same as above
ZZZ=Top.reshape(2161,4321) #set the topography into a nice shape too


fig1=plt.figure()
ax=fig1.add_subplot(111)
ax.set_aspect(1)
ax.set_title('World Topography')
pcm=ax.pcolormesh(XXX,YYY,ZZZ, cmap=plt.cm.RdBu_r) ## deosn't like this, "cannot perform reduce with flexible type"
ax.contour(XXX,YYY,ZZZ,[-1000,0,1000], colors=['black','black','black'], linewidths=[1,2,1], linestyles=['dashed','solid','solid'])#finally this is behaving, even if the pcolor isn't
fig1.show()

#the pcolor isn't centered at zero, I'll have to look up how to fix that later
