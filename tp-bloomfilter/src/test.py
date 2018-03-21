# -*- coding: utf-8 -*-

""":mod:`test` module : Test module for bloomfilter analysis

:author: `FIL - IEEA - Univ. Lille1.fr <http://portail.fil.univ-lille1.fr>`_

:date: 2016, january

"""
import random
import bloomfilter

nb_hash_functions = 8
random_tab = [ 0 for i in range(128 * nb_hash_functions)]

def init_random_tab ():
    """
    Creates the hash functions.
    """
    global random_tab
    for i in range(128):
        for j in range(nb_hash_functions):
            random_tab[j * 128 + i] = random.randint(1,32000)

def code_of_string (str,n):
    """
    For a given string, returns the hash code for the n-th hashing function.

    :param str: The string to be hashed.
    :type str: string
    :param n: The function number.
    :type n: int
    :return: A hash code
    :rtype: int

    .. note::
       1 <= n <= nb_hash_functions
    """

    h = 0
    for e in str:
        h+=random_tab[ord(e)+(n*128)]
    return h


def random_word ():
    """
    Returns a word with random letters whose length is between 4 and 7.

    :rtype: string
    """
    letters = [ chr(i) for i in range(ord('a'),ord('z')+1) ] + [ chr(i) for i in range(ord('A'),ord('Z')+1) ]
    length = 4 + random.randint(0,4)
    str = ""
    for i in range(length):
        str = str + random.choice(letters)
    return str

def test():
    resultat=""
    file=open('res.txt','w')
    faux_pos=0;
    mot_test=0
    I=list()

    for i in range(0,10):
        I.append(random_word())
        
    for n in range(1,8):
        for t in range(10,20):
            resultat=""
            bf = bloomfilter.create(t,code_of_string,n)
            for i in I:
                bloomfilter.add(bf,i)
            for k in range(1,2**14):
                U=random_word()
                if not(U in I):
                    mot_test+=1
                    if(bloomfilter.contains(bf,U))  :
                        faux_pos+=1
            resultat+= str(t)+" " + str(n)+" " + str(k)+" " + str(mot_test)+" " + str(faux_pos)+" " + str(faux_pos/k)+"\n"    
            file.write(resultat)    
        file.write('\n\n')
    file.close()

if __name__ == "__main__":
    init_random_tab()
    bf = bloomfilter.create(6,code_of_string,8)
    w = random_word()
    bloomfilter.add(bf,"timoleon")
    if bloomfilter.contains(bf,"timoleon"):
        print("%s est present" % ("timoleon"))
    if bloomfilter.contains(bf,w):
        print("%s est present" % (w))

    #test code_of_string
    #print(code_of_string("toto",1))
    
    test()
