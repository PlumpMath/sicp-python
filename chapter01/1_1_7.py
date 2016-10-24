from __future__ import division


def sqrt_iter(x):
    """
    """
    
    guess = 1
    while abs(guess**2-x) > 0.001:
        guess = (x/guess + guess)/2
        
    return guess
