'''
   Compute the entropy on files.

   @author FIL - IEEA - Univ. Lille 1 (oct 2010, août 2015)
'''

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
    counters = {}
    nb_bytes = 0
    infile = open(filename, 'rb')
    byte = infile.read(1)
    # A COMPLETER

    # 2) Calcul de l'entropie à partir des effectifs des octets.
    total_sum = 0
    # A COMPLETER

    return # A COMPLETER

def usage():
    print("Usage: {:s} <filename>".format(sys.argv[0]))
    print("\t<filename>: filename for which we want to compute the entropy.\n")
    exit(1)

def main():
    if len(sys.argv) != 2:
        usage()
    (nb_bytes, entro) = entropy(sys.argv[1])
    print("{:d} bytes read.".format(nb_bytes))
    print("Entropy = {:f} bits per byte.".format(entro))
    
if __name__ == '__main__':
    main()
