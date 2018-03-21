# -*- coding: utf-8 -*-

"""
:mod:`experience` module : Module to manages markers and experiences

:author: `FIL - IEEA - Univ. Lille1.fr <http://portail.fil.univ-lille1.fr>`

:date: 2015, december

A marker is a represented as a String. An exeperience is simply a list of 
positive markers selected from a list of markers.

"""

import random
import copy

def markers (p):
    """
    Returns a list of *p* markers. Markers are in random ordering.

    :param p: The number of markers (must be strictly greater than 0.
    :type p: int
    :return: The list of markers
    :rtype: List of String
    
    >>> markers(10)
    ['m9', 'm1', 'm7', 'm2', 'm4', 'm0', 'm6', 'm8', 'm5', 'm3']
    """
    assert(p > 0)
    l = [ "m%d" % (i) for i in range(p) ]
    random.shuffle(l)
    return l

def experience (p,m):
    """
    Produces the results of an experience on *p* positive markers
    among the list of *m* markers.

    :param p: The number of positive markers (must be less or equal 
        than the numbers of markers in *m*
    :type p: int
    :param m: The list of markers
    :type m: List of String
    :return: The list of positive markers.
    :rtype: List of String

    >>> experience(10,markers(100))
    ['m16', 'm79', 'm18', 'm13', 'm26', 'm6', 'm11', 'm17', 'm29', 'm77']    
    """
    assert (p <= len(m))
    l = copy.deepcopy(m)    
    random.shuffle(l)
    return l[0:p]


def compare (m1,m2):
    """
    Compares markers *m1* and *m2*.

    :param m1: The first marker
    :type m1: String
    :param m2: The first marker
    :type m2: String
    :return: -1, 0 or 1 resp. if *m1 < m2*, *m1* = *m2* or *m1* > *m2*
    :rtype: int
    
    >>> compare("m45","m234")
    -1
    >>> compare("m45","m45")
    0
    >>> compare("m45","m4")
    1
    """
    if m1 == m2:
        return 0
    elif m1 < m2:
        return -1
    else:
        return 1

    
if __name__ == "__main__":
    print(markers(10))
    print(experience(10,markers(100)))
    
