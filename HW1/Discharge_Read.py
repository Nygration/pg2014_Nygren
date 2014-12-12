"""
Created on Fri Sep 19 14:18:24 2014
@author: Nygren
Part 3 read in the data from the file discharge.dat and return a list of datetimes (as datetime objects) and discharge (ignoring any flags)
"""
"""http://raw.github.com/Hetland/pg2014/master/HW1/discharge.dat"""
"""raw file now in documents folder discharge.dat"""
def discharge_read(filename):
    """This function will be able to read in the data from discharge.dat and return a list of datetimes and discharge ignoring flags (I assume this means remove the _A, _P or _e_A and just give the number)"""
    import datetime # if we want to use datetimes we should probably import this
    import numpy as np # not sure if this is needed for loadtxt or not, but It was used in class so...
    
    dataraw=np.loadtxt(filename, dtype=u"string") # this loads the data as it was formatted into a variable creating a list of lists(lines) where the inner list gives 'the station type' 'station number' 'date' and 'discharge_flag'
    readable_list=[] # I'll initialize the list I'll return here and then append it
    
    for i in range(0,len(dataraw)): # just running through the list
        idate=datetime.datetime(year=int(dataraw[i][2][0:4]),month=int(dataraw[i][2][5:7]),day=int(dataraw[i][2][8:10])) # this makes datetime variable from the characters in the string
        idischarge=dataraw[i][3][0:(dataraw[i][3].index('_'))]# take the numbers before the underscore (used aspart of the flag)
        paired_data=[idate, idischarge] # pair the discharge with its date (how am I still single when even the discharge can get a date?)
        readable_list.append(paired_data)
    
    return readable_list # returns the list of paired dates and discharges it takes a little while as 

if __name__ == '__main__':
    thefile='discharge.dat'
    datapairs=discharge_read(thefile)
    print datapairs[:5] #print the 1st 5 data pairs