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

    multi=128
    inc = 0
    retour = 0
    byte=[bin(bytes_read[0])[2:].zfill(8) , bin(bytes_read[1])[2:].zfill(8) , bin(bytes_read[2])[2:].zfill(8)]

    while inc <8 :
        if byte[0][inc]== byte[1][inc] or byte[0][inc]== byte[2][inc] :
            retour=retour+ int(byte[0][inc]) * multi
        elif byte[1][inc]== byte[2][inc]:
            retour=retour+ int(byte[1][inc]) * multi
        multi = multi // 2
        inc+=1
    return (int(retour))

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
    retour=0
    byte=[bin(bytes_read[0])[2:].zfill(8) , bin(bytes_read[1])[2:].zfill(8) , bin(bytes_read[2])[2:].zfill(8)]
    x=bin(majority(bytes_read))[2:].zfill(8)
    while(inc<8):
        if(x[inc]!=byte[0][inc] or x[inc]!=byte[1][inc] or x[inc]!=byte[2][inc]):
            retour+=1
    return retour
if __name__ == '__main__':
    import doctest
    doctest.testmod()
