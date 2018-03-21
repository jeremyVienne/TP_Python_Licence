#!/usr/bin/env python3

from math import *

def taille (x):
    i=1+log10(floor(x))
    #len(str(floor(x)))
    return i
    
print(floor(taille(float(input("Chiffre positif svp: ")))))




