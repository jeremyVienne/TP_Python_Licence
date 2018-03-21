#!/usr/bin/env python3
"""
:author: Vienne & Lecornet
:date: 20/09/16
:object: representation of numbers
"""

def integer_to_digit(entier):
    """
    Parameters:	integer (int) â€“
    Returns: the character representing the hexadecimal digit
    Return type: str
    CU:	integer >= 0 and integer < 16
    """
    assert ( (entier >=0) and (entier<=15) )
    return "{:X}".format(entier)

def integer_to_string(n,b):
    """
    Parameters:	integer (int) â€“ the integer we want to representbase (int) â€“ the base in which the integer must be represented
    Returns: The string representation of the integer given in parameter in base base.
    Return type: str
    CU:	base >= 2 and base <= 16 and integer >= 0
    """
    assert ( b>1 )
    assert ( n>=0 )
    r=n%b
    q=n//b
    fin=str(r)
    while (q>=b):
        r=q%b
        q=q//b
        fin=fin+str(r)
    fin=fin+str(q)
    return fin[::-1]

def deux_puissance(n):
    """
    Parameters:	n (int) – The power of two
    Returns:The value of 2^n
    Return type:int
    CU: n >= 0
    """
    return 1<<n

def integer_to_binary_str(entier):
    """
    Parameters:	integer (int) – the integer to be converted in binary
    Return type:str
    Returns:Return the binary representation (as a string) of integer
    CU:	integer >= 0
    """
    retour=""
    tmp=""
    while (entier>0):
        if(entier&1):
            tmp="1"
        else:
            tmp="0"
        retour = tmp + retour
        entier = entier>>1
    return retour

def binary_str_to_integer(binary):
    """
    Parameters:	bin_str (str) – The input binary string
    Returns:The integer whose binary representation is bin_str
    Return type:int
    CU:	bin_str is a binary string (containing only 0s or 1s).
    """
    retour=0
    inc=0
    while (inc<len(binary)):
        tmp=0
        if(binary[inc]=="1"):
            tmp=1
        retour=(retour<<1)|tmp
        inc=inc+1
    return retour

if __name__ == "__main__":
    import doctest
    doctest.testmod()
        

    # 1.1 Impression des entiers avec print

    print("\n1.1 Q1\n")
    entier = 4242
    print (entier,"entier de base")
    print ("{:x} {:o} {:X}".format(entier,entier,entier),"=> :x :o :X")

    print("\n1.1 Q2\n")
    entier = 1331
    print (bin(entier),"bin")
    print (oct(entier),"oct")
    print (hex(entier),"hex")

    #1.2 Transformer un entier en un chiffre

    print("\n1.2 Q3\n")
    for n in range(1,15):
        print (chr(ord('0') + n))
        # 0<n<10 vaut les chiffres de 1 Ã  9
        # 9<n<... vaut des caractÃ¨res tel que : ; < = > ...
        
    print("\n1.2 Q4\n")
    for n in range(10,16):
        print (chr(ord('0') + n +7))

    print("\n1.2 Q5\n")
    for n in range(0,16):
        print(integer_to_digit(n))
    
    #1.3 Convertir un entier en une chaÃ®ne de caractÃ¨res
        
    print("\n1.3 Q6\n")
    print(integer_to_string(15,2))
    print(integer_to_string(100,16))
    print(integer_to_string(42,10))
    
    print("\n1.3 Q7\n")
    for nb in range(0,21):
        print ("{:2d} : {:>6s} {:>3s} {:>3s}".format(nb,integer_to_string(nb,2),integer_to_string(nb,8),integer_to_string(nb,16)))

    #2.1 Les opÃ©rateurs logiques sur les entiers en Python

    print("\n2.1 Q8\n")
    print((4>2) & (8>6))
    print((4>2) | (1>5))
    print((4>2) ^ (8>6))
    print(~(4))
    print(bin(0b1010<<2))
    print(bin(0b1001>>2))
    
    print("\n2.1 Q9\n")
    print("n << 1 signifie qu'on decale l'écriture binaire de 'n' d'un bit vers la gauche")
    print("n >> 1 signifie qu'on decale l'écriture binaire de 'n' d'un bit vers la droite")
    
    print("\n2.1 Q10\n")
    test=4
    print("2^n avec n="+str(test)+" => "+str(deux_puissance(4)))

    print("\n2.1 Q11\n")
    chiffre=0b10101
    if (chiffre&1):
        print(str(bin(chiffre))+"est impaire")
    else:
        print(str(bin(chiffre))+"est paire")

    print("\n2.2 Q12\n")
    test=25
    print(str(test)+"="+integer_to_binary_str(test))
    
    print("\n2.2 Q13\n")
    test=integer_to_binary_str(25)
    print(test+"="+str(binary_str_to_integer(test)))
    
