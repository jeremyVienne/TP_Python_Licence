# -*- coding: utf-8 -*-

"""
:mod:`test` module : test module for experiences assignment

:author: `FIL - IEEA - Univ. Lille1.fr <http://portail.fil.univ-lille1.fr>`_

:date: 2015, december
"""

import sys
import experience
import sorting 

def compare (m1,m2):
    return experience.compare(m1,m2)

# STRATEGY 1
def negative_markers1(markers,positive):
    """
    Computes the list of negative markers from the list of markers and
    the list of positive markers.

    :param markers: The list of markers
    :type markers: List of String
    :param positive: The list of positive markers
    :type positive: List of String
    :return: The list of negative markers
    :rtype: List of String
    """
    negative = []
    inc=0
    for m in markers:
        
        for p in positive:
            inc+=1
            if (m==p):
                return inc,negative
        
        negative.append(m)
        
    return inc,negative

# STRATEGY 2
def negative_markers2(markers,positive):
    positive=sorting.merge_sort(positive,compare)
    return negative_markers1(markers,positive)
  

# STRATEGY 3
def negative_markers3(markers,positive):
    markers=sorting.merge_sort(markers,compare)
    
    return negative_markers2(markers,positive)



def ee(inc):
    """
    structure the number in parameter to be returned in a 3 caracter string
    """
    if inc<10:
        return "  "+str(inc)
    elif inc<100:
        return " "+str(inc)
    else:
        return str(inc)

def print(value):
    file = open("fichier10.txt","a")
    file.write(value+"\n")
    file.close()
    
if __name__ == "__main__":
    p = int(sys.argv[1])
    m = int(sys.argv[2])
    n=10
    try :
        n= int(sys.argv[3])
    except:
        n=n
        
    markers = experience.markers(m)
    positive = experience.experience(p,markers)

    print("Markers: %s" % (markers))
    print("Positive markers: %s" % (positive))
    
    # test stategy 1
    cmp,negative=negative_markers1(markers,positive)
    print("Negative markers: %s" % (negative))
    print("Nb. comparaisons: %d" % (cmp))

    # test stategy 2
    cmp,negative=negative_markers2(markers,positive)
    print("Negative markers: %s" % (negative))
    print("Nb. comparaisons: %d" % (cmp))

    # test stategy 3
    cmp,negative=negative_markers3(markers,positive)
    print("Negative markers: %s" % (negative))
    print("Nb. comparaisons: %d" % (cmp))

    for i in range (1,n+1):
        markers=experience.markers(m)
        positive=experience.experience(p,markers)
        cmp1,negative=negative_markers1(markers,positive)
        cmp2,negative=negative_markers2(markers,positive)
        cmp3,negative=negative_markers3(markers,positive)
        print("%d %s %s %s %s" %(n,ee(i),ee(cmp1),ee(cmp2),ee(cmp3)))
     
