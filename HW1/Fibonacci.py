"""
Created on Fri Sep 19 13:37:12 2014
@author: Nygren
part 1 create a function that will take argument n and return a series of fibonacci numbers of length n
"""

def fibn(n,x=1,y=1):
    
    """ argument n will be used to determin the length of the series returned
    argument x will be defaulted to one and will be the first number used
    argument y will be defaulted to one and will be the second number used
    these arguments are available as fibonacci sequences do not nessecarily have to start with 1 and 1. """  
    fiblist=[] # initialize the list, we will add to it depending on the requested length
    holder1=x # a place holder to keep track of the second to last number in the list
    holder2=y # a place holder to keep track of the last number in the list
    newsum=0 # This will be the sum of two place holders and be appended to the list
    if (n<1):   # on the off chance they do something dumb, tell them that
        print "Why would you do that? You know what? Just for that, you get NOTHING!"
    if (n==1): # to handle the issue of someone not wanting more than one, I feel like there should be a way to say "do this" then with the next if statement just "also do this" but I don't know one yet
        fiblist.append(holder1)
    if (n>1):   # will update the list with the requested start values and begin the fibonacci itteration 
        fiblist.append(holder1)     # add the first number
        fiblist.append(holder2)     # add the second number
        while (len(fiblist)<(n)):   # ensure there are as many numbers as requested
            newsum=holder1+holder2  # sum the last two numbers on the list
            fiblist.append(newsum)  # update the list with the new sum            
            holder1=holder2         # point at the new 2nd to last number on the list
            holder2=newsum          # point at the new last number in the list
    return fiblist                   # GIVE 'EM WHAT THEY WANT!

if __name__=='__main__':
    print fibn(10) #print the 1st ten numbers in the sequence