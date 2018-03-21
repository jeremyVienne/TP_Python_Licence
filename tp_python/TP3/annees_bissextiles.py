#/usr/bin/env pyhton3
from math import *

def est_divisible_par(x,y):
    return floor(x/y)

def est_bissextile(an):
    if (est_divisible_par(an,4)==True and (est_divisible_par(an,100)==False or (est_divisible_par(an,400)==True)
    
