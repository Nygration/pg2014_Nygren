# -*- coding: utf-8 -*-
"""
Created on Sun Oct 12 22:28:24 2014
@author: Chris Nygren
HW2P3 Create a 'high-pass' filter function that removes a trend from a given series of points using a polynomial fit of order N (specified as a functional input, default is N=1 for a linear fit).
The function returns the difference between the given series and the polynomial fit.
"""
import numpy as np

def PolyNoise(data, NNN=1):
    """For this function, the data had better be as a list of paired coordinates
    as an Nx2 Matrix 
    """
    
    xxx=data[:,0]
    yyy=data[:,1]
    fit=np.polyfit(xxx,yyy,NNN)
    polyyy=np.polyval(fit,xxx)
    noiseyyy=yyy-polyyy
    return np.vstack((xxx,noiseyyy)).T
    
