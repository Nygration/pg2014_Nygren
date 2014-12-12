"""
Created on Fri Sep 19 13:37:12 2014
@author: Nygren
part 2 write a function that computes the integral of a list of numers by the trapazoidal rule with a default value of dx=1.0 
"""
def integrate(f,dx=1.0):
    """This function will take a list of numbers as an argument f, and integrate using the trapezoidal rule """
    return (dx*sum(f)-((f[0]+f[-1])/2)) # trapazoidal just adds a half the sum of two numbers, and runs through so it adds two halves of each number except the fist and last. 
        
if __name__=='__main__':
    example=[1,3,4,5] # make a list of numbers
    print integrate(example) # integrate