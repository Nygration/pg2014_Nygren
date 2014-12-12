"""
Created on Sun Sep 21 20:22:47 2014
@author: Nygren
This is the advanced bit. This function should be rtead data from drifter.dat and return a dictionary based on the track name and indices, returning a list of lat lon pairs. 
"""
def read_drifter(filename):
    """ This should read in the file drifter.dat and return a dictionary based on the track indices, returning a list of lat/lon pairs"""
    
    import numpy as np  # for the loadtxt command
    
    rawfile=open(filename) # gives me something to work with, keeping the formatting of the original file
    filestring=rawfile.read() # reads in the file, but for some reason there is extra white space between each character, very aggrivating
    #cleanfilestring=filestring[::2] # it looks like the blank space is after every character so I'll remove all the even indexed characters, still not sure where the wierd character at the beginning came from
    lines1=filestring.split("\n") # break it into lines
    thedictionary={} # empty dictionary that I'll add keys to
    keyname=' ' # empty key name that I'll fill when I get a new key and then use it in the for loop to fill the values.
    #keylist=[] # an empty list that I will append and set equal to the current key
    for i in range(0,len(lines1)):  # go through the lines 
        if (lines1[i][0:6]=="Track\t"): # and if the first 6 letters are "Track    " (convenient way to grab the data with the track names) then do the following
            keyname=(lines1[i][(lines1[i].index('\t')+1):lines1[i].index('\t',(lines1[i].index('\t')+1),-1)]) # keep the part of the line after the first tab and before the second tab
            thedictionary.setdefault(keyname,[]) #add the key name to the dictionary and initialize the value as a list
        if (lines1[i][0:6]=="Trackp"): # and if the first 6 letters are "Trackp" then they are the lats/lons and we will add then to whatever the current list is (list is always initialized before the data shows up)
            latlonstring=(lines1[i][(lines1[i].index('\t')+1):lines1[i].index('\t',(lines1[i].index('\t')+1),-1)]) # keeps the data we want (between the first two tabs), cuts the stuff we don't want 
            latlonparts=latlonstring.split(' ') # this will break the string into lat:deg, min, lon:deg, min
            latlon=(float(latlonparts[0][1:])+(float(latlonparts[1])/60),float(latlonparts[2][1:])+(float(latlonparts[3])/60)) # makes a tuple of the lat and lon in degree form (it does lack the cardianl direction, but thats what the example has...)
            thedictionary[keyname].append(latlon) # add the new lat/lon pair to the current list
    return thedictionary # return the dictionary they want

drifterfile='drifter.dat' #choose the correct file
drifterdict=read_drifter(drifterfile) #make the dictionary
print drifterdict.keys() # print all the keys (frodo, samwise, etc.)
