#!/usr/bin/env python3
from math import *

def afficher_debut(x):
    a0=floor(x)
    y=1/(x-a0)
    
    a1=floor(y)
    z=1/(y-a1)
    a2=floor(z)

    print(a0,"\n", a1, "\n", a2)
    print( a0, " + 1 / ( ", a1, " + 1 / ",a2, " )")
    print("Pi= ", a0+1/(a1+1/a2))
    
    
afficher_debut(pi)

