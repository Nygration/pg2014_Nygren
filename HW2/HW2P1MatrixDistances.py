""" HW2 problem1
Python for geoscientists
Author: Chris Nygren
15:44 10/9/2014

This will take two matrixes of dimensions Nx2 and Mx2, 
containing coordinate pairs, 
and return an NxM matrix of distances from the points in one matrix
to the points in the other. All without using loops
Input:
matrix 1: of dimensions Nx2 of coordinate pairs
matrix 2: of dimensions Mx2 of coordinate pairs
Output: 
matrix 3: of dimensions NxM containing distances between points
"""
import numpy as np 

def dist_list(matrix1,matrix2):
	MMM=np.array(np.split(matrix2,len(matrix2[:,0])))
	NNN=matrix1-MMM
	OOO=np.sqrt((NNN[:,:,0]**2)+(NNN[:,:,1]**2))
	return OOO.T
	