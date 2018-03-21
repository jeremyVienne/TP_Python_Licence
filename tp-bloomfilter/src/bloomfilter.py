# -*- coding: utf-8 -*-

""":mod:`bloomfilter` module : Implements a bloomfilter.

:author: `FIL - IEEA - Univ. Lille1.fr <http://portail.fil.univ-lille1.fr>`_

:date: 2016, january

"""

def create (n,f,m):
    """
    Creates a new empty Bloom filter of size :math:`2^n`

    :param n: the log of the size of the filter
    :type n: int
    :param f: the hash function whose should take as input two 
              parameters: the value to be hashed and the number 
              of the subfunction used
    :type f: function(any,int)
    :param m: the number of functions provided by *f*
    :return: the new Bloom filter
    :rtype: dict
    """
    table = [False]*(2**n)
    bloom=dict()
    bloom["table"]=table
    bloom["f"]=f
    bloom["m"]=m
    
    return bloom

def add (bf, e):
    """
    Adds *e* to *bf*.

    :param bf: A Bloom filter
    :type bf: dict
    :param e: The element to be added
    :type e: Any
    """
    
    
    for i in range (bf["m"]):
        bf['table'][bf["f"](e,i)%(len(bf["table"]))]=True
        
def contains (bf, e):
    """
    Returns True if *e* is in *bf*.

    :param bf: A Bloom filter
    :type bf: dict
    :param e: The element to be tested
    :type e: Any
    """
    tjrs_vrai=True

    for i in range (bf["m"]):
        if not (bf['table'][bf["f"](e,i)%(len(bf["table"]))]):
            tjrs_vrai=False
    return tjrs_vrai


    
