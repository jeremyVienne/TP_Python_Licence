'''
Implementing a binary symmetric memoryless channel (CBSSM)

:author: FIL - IEEA - Univ. Lille 1 (nov 2010, août 215)
'''
import random

class Not_a_proba(Exception):
    pass

class Not_a_byte (Exception):
    pass

def noise (p):
    '''
    Return a 1-bit with probability `p`

    :param p: Probability of having a 1
    :type p: float
    :return: A bit
    :rtype: int
    :UC: p >= 0 and p <= 1
    :Examples:

    >>> noise(0)
    0
    >>> noise(1)
    1
    '''
    if random.random() < p:
        return 1
    else:
        return 0

def cbssm(p, byte):
    '''
    Transmit a byte through a CBSSM and return the received byte.

    :param p: Probability of having an error in the CBSSM
    :type p: float
    :param byte: The byte to be transmitted
    :type byte: int
    :return: `byte` where each bit was modified with a probability `p`
    :rtype: int
    :UC: p >= 0 and p <= 1 and byte >= 0 and byte < 256
    '''
    if p < 0 or p > 1:
        raise Not_a_proba(p)
    if byte < 0 or byte > 255:
        raise Not_a_byte(byte)
    error_vector = 0
    for pos in range(8):
        error_vector = (error_vector << 1) | (noise(p))
    return error_vector ^ byte

random.seed()



#cbssm(0,48)
#48

#cbssm(1,48)
#207
