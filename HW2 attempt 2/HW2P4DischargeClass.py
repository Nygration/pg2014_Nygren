# -*- coding: utf-8 -*-
"""
Created on Sun Oct 12 23:58:36 2014
@author: Chris Nygren
Make a class to read discharge data for the Brazos river from  
http://waterdata.usgs.gov/nwis/dv?cb_00060=on&format=rdb&site_no=08116650&referred_module=sw&period=&begin_date=1967-10-01&end_date=2014-10-01
Store date as an array and discharge data (cubic meters per second) as an array, both attributes of the class
make methods to:
    extract a year of discharge data, return dates and discharges for the specified year
    calculate annual mean discharge return on array of years and mean discharges
    plot the hydrography over the entire length of the timeseries
"""
url='http://waterdata.usgs.gov/nwis/dv?cb_00060=on&format=rdb&site_no=08116650&referred_module=sw&period=&begin_date=1967-10-01&end_date=2014-10-01'
dischargefilename='C://Users/User/Documents/Class notes/python/HW2discharge.dat'
import numpy as np
import datetime
import matplotlib.pyplot as plt
                #shouldn't have to mess with anything below this line)#
############################################################################################################################################################################################################################################

class DischargeData(object):
    """This class will read in the data from a file given to it and will have attributes of Dates and Discharge which will be arrays of datetime objects and floats respectively. 
    The discharge will be in meters cubed per second
    """
    
    def __init__(self,filename):    
        rawdata=np.loadtxt(filename, dtype=u"string") ##for some reason there is a lot of data missing from OCt 1981 to Apr. 1984
        self.Discharge=np.ndarray(shape=(len(rawdata[:,0])), dtype=float)
        self.Dates=np.ndarray(shape=(len(rawdata[:,0])), dtype=datetime.datetime)  # initializes the array that will hold the datetime objects (not sure why we don't use date objects, but I just do what I'm told)
        for k in np.arange(0,len(rawdata[:,0])):  #For each freakin line in the data read in what I want.
            self.Dates[k]=datetime.datetime(year=int(rawdata[k,2][0:4]),month=int(rawdata[k,2][5:7]),day=int(rawdata[k,2][-2:])) #changesthe strings to ints so they can be read in to the various data types associated with the datetime object
            self.Discharge[k]=float(rawdata[k,3])*(0.0283168)      ##this takes the discharge in ft^3 s^-1 and puts it in m^3 s^-1            
            #had to do it in a loop instead of feeding it an array because the int() function doesn't like itterating, what a jerk.
            #also it didn't like the idea that multiplying an array by a float should jsut be element wise multiplication with the float...
        print self.Dates.shape,self.Discharge.shape
    
    def Year(self,year1):
        start=np.where(self.Dates==datetime.datetime(year=year1,month=1,day=1)) #finds the index of the first entry (Jan 1st) of that year
        end=np.where(self.Dates==datetime.datetime(year=year1+1,month=1,day=1)) #finds the index of the first entry (Jan 1st of the year after    
        yeardata=np.vstack((self.Dates[start[0]:end[0]],self.Discharge[start[0]:end[0]])).T   #gives the dates and discharge for everything from the beginnign(Jan 1st) of the given year, up to but not including the beginning (Jan1st) of the next year
        return yeardata #this will not work with the missing data as np.where returns all that meet the condition so >= Dec31st doens't work well. IT has to be date specific
        # if time allows I will try to make this work with the missing data by getting the condition to get the indexes from the earliest data in the year to the last data in that year. 
        
        
    def Plot(self):
        fig1=plt.figure()
        ax=fig1.add_subplot(111)
        ax.plot(self.Dates,self.Discharge,'k-')
        ax.set_ylabel('Discharge (m³/s)')
        ax.set_xlabel('Date (data missing from Oct 1980 to Apr 1984)')
        ax.set_title('Brazos River Discharge')
        fig1.show()
        
Brazos=DischargeData(dischargefilename)

