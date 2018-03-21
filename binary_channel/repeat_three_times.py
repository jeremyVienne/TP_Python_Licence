#!/usr/bin/env python3
"""
:author: Vienne
:date:29/11/2016
:object: repeat three times
"""

def encode(byte):
    """
    Encode the byte using repetition coding

    Parameters:	byte (int) – The byte to encode
    Returns:	A list of three bytes equal to byte
    Return type:	list
    UC:	0 <= byte < 256
    Examples:	
    >>> encode(123)
    [123, 123, 123]
    >>> encode(0)
    [0, 0, 0]
    """
    assert byte >= 0 and byte<256,"byte compris entre 0 et 255"
    return [byte,byte,byte]

def decode(bytes_read):
    """
    Takes three bytes (encoded with repetition three times) and return a byte plus some information on the number of errors

    Parameters:	bytes_read (bytes) – Three bytes
    Returns:	A tuple of three elements. The first element is the byte made with the majority bits of the three bytes. The second element is the number of detected errrors. The last element is the number of corrected errors (both numbers are equal here).
    Return type:	tuple
    UC:	len(bytes_read) == 3
    Examples:	
    >>> decode(bytes([0b00100001, 0b10100011, 0b10000000])) == (0b10100001, 4, 4)
    True
    """
    assert len(bytes_read)==3, "len(bytes_read) ==3"
    return(majority(bytes_read), nb_errors(bytes_read), nb_errors(bytes_read))

def majority(bytes_read):
    """
    Parameters:	bytes_read – Three bytes
    Type:	bytes
    Returns:	The returned byte is constituted of the majoritarian bits among the three bytes
    Return type:	int
    UC:	len(bytes_read) == 3
    Examples:	
    >>> majority(bytes([0b00100001, 0b10100011, 0b10000000])) == 0b10100001
    True
    >>> majority(bytes([0b00000000, 0b10101010, 0b01101101])) == 0b00101000
    True
    """
    assert len(bytes_read) == 3 , "len(bytes_read) == 3"

    byte=list(bytes_read)
    resultat=0
    inc=0

    while(inc<8):
        nb1=0
        for i in range(0, len(byte)):
            if(byte[i] & 1 ==1):
                nb1+=1
            byte[i]=byte[i] >> 1
        if (nb1 >= 2):
            resultat=resultat | (1<<inc)      
        else:
            resultat=resultat | (0<<inc)              
        inc+=1
    return resultat

def binary_weight(w):
    """
    Parameters:	w (int) – A number
    Returns:	The binary weight (ie. the number of 1 in the binary representation of w).
    Return type:	int
    Examples:	
    >>> binary_weight(1)
    1
    >>> binary_weight(0)
    0
    >>> binary_weight(2)
    1
    >>> binary_weight(5)
    2
    >>> binary_weight(2048)
    1
    """
    
    retour=0
    for i in bin(w):
        if(i=='1'):
            retour+=1
    return retour
    

def nb_errors(bytes_read):
    """
    Parameters:	bytes_read (bytes) – Three bytes
    Returns:	The total number of errors among the bytes in bytes_read That corresponds to the number of positions where bits differ among the three bytes
    Return type:	int
    UC:	len(bytes_read) == 3
    Examples:	
    >>> nb_errors(bytes([0b01, 0b10, 0b11]))
    2
    >>> nb_errors(bytes([0b0011100, 0b0010111, 0b1001000]))
    6
    """
    inc = 0
    l=list(bytes_read)
    byte_majo=majority(bytes_read)
    nb_erreur=0
    while(inc <8):
        bit=byte_majo & 1
        for i in range(0, len(l)):
            b=l[i] &1
            
            if(b!=bit):
                nb_erreur+=1
                
            l[i]=l[i]>>1
        byte_majo=byte_majo>>1
        inc+=1
    return nb_erreur
if __name__ == '__main__':
    import doctest
    doctest.testmod()
