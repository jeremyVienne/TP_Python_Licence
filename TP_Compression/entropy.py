#!/usr/bin/env python3
"""
:author: Vienne & Lecornet
:date: 20/09/16
:object: compression
"""
'''
   Compute the entropy on files.

   @author FIL - IEEA - Univ. Lille 1 (oct 2010, août 2015)
'''
from math import log2
import sys

# IMPORTS A COMPLETER


def entropy(filename): 
    '''
    Computes the entropy of the file called `filename`.

    :param filename: Input file name.
    :type filename: str
    :return: A tuple whose first element is an integer: the number of bytes read\
    and the second element is a float: the entropy of the file's content
    :rtype: tuple
    '''

    # 1) Read the file to count occurrences of each byte
    # Dictionary that will store the number of occurrences of each byte.    
    counters ={}
    nb_bytes = 0
    infile = open(filename, 'rb')
    #byte = infile.read(1)

    while(infile.read(1)):
        nb_bytes+=1
        
    
    # 2) Calcul de l'entropie à partir des effectifs des octets.
    

    infile.seek(0)
    ns=""
    inc=0
    while(infile.read(1)):
        infile.seek(inc)
        ns=infile.read(1)
        if (ns in counters):
            counters[ns]+=1
        else:
            counters[ns]=1
        inc+=1

    tmp=0
    entro=0
    for i in counters:
        tmp+=(counters[i]*log2(counters[i]))

    entro=log2(nb_bytes)- (tmp/nb_bytes)
    opti=0
    opti=entro/log2(256)
    return nb_bytes, entro, opti

def usage():
    print("Usage: {:s} <filename>".format(sys.argv[0]))
    print("\t<filename>: filename for which we want to compute the entropy.\n")
    exit(1)

def main():
    if len(sys.argv) != 2:
        usage()
    (nb_bytes, entro, opti) = entropy(sys.argv[1])
    print("{:d} bytes read.".format(nb_bytes))
    print("Entropy = {:f} bits per byte.".format(entro))
    print("An optimal coding would reduce this file size by ", (1-opti)*100, "%")
    
if __name__ == '__main__':
    main()
    #Question1:
    #la valeur maximale de l'entropie est 8 (log(2)256=8)
    #chacun des 256 octets est présents un meme nombre de fois dans le fichier

    #Question 2:
    #TP_compression_1_2.pdf

    #test 1:
    #python3 entropy.py entropy_skeleton.py

    #1309 bytes read
    #Entropy= 4.829613 bits per byte
    #An optimal coding would reduce this file size by 39.62983461112762%

    #test 2:
    #python 3 entropy.py cigale1.txt

    #624 bytes read
    #Entropy = 4.630460 bits per byte
    #An optimal coding would reduce this file size by  42.11925142087798 % 
