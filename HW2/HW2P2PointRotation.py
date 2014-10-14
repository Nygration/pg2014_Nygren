# -*- coding: utf-8 -*-
"""
Created on Sun Oct 12 20:19:41 2014
@author: Chris Nygren
HW2P2 Using the point class from class add a method that rotates the point clockwise by a specified number of radians
about another optional point defaulting to the origin. 
"""

from math import sqrt
from math import atan
from math import sin
from math import cos
from numpy import pi



class Point(object):
    """docstring for Point
For the rotate method inputs are radians you want to rotate, and optionally another point you want to rotate around, if not the origin
note that the term self.x-xxx and self.y-yyy are used. and at the end xxx and yyy are added back in. 
This effectively shifts the origin to the point selected and then shifts it back at the end.
The atan function only returns values between -pi/2 and pi/2 so if self.x-xxx is negative then an extra pi radians need to be added to get back to the correct quadrant
This function will change the coordinates of the point given so if you want to keep the original point you should make a new one like <point name>=<orginal point name.rotate(etc.)
    """
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def norm(self):
        return sqrt(self.x**2 + self.y**2)
    
    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y)
        
    def rotate(self, radians, other=None):
        if other==None : #This bit handles if it will be rotated around another
            xxx=0.0      #point
            yyy=0.0
        else :
            xxx=other.x
            yyy=other.y
        check=0         #this will ensure it is in the correct quadrant later
        if (self.x-xxx) < 0: #its necessary because atan only returns values 
            check=1          #between -pi/2 and pi/2 so sometimes you need to
        angle=atan((self.y-yyy)/(self.x-xxx)) - radians +(check*pi) #add pi
        CCC=sqrt((self.y-yyy)**2 + (self.x-xxx)**2) #Note the self.Q-qqq in the
        self.x=(CCC*cos(angle))+xxx                 #case we rotate around 
        self.y=(CCC*sin(angle))+yyy                 #another point
        
