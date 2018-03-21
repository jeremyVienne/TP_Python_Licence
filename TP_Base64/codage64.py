#!/usr/bin/en python3


"""
:author: Vienne Jeremy & Lecornet Didrick
:date: 20/09/16
:object: base64
"""


from os import sys

BASE64_SYMBOLS=["A", "B", "C", "D", "E", "F", "G", "H",
"I", "J", "K", "L", "M", "N", "O", "P",
"Q", "R", "S", "T", "U", "V", "W", "X",
"Y", "Z", "a", "b", "c", "d", "e", "f",
"g", "h", "i", "j", "k", "l", "m", "n",
"o", "p", "q", "r", "s", "t", "u", "v",
"w", "x", "y", "z", "0", "1", "2", "3",
"4", "5", "6", "7", "8", "9", "+", "/"]


#Question 4:
def bytes_to_symbols(octets):
    """
    Takes (at most) three bytes of data in input and returns the corresponding bas64 symbols.

    Parameters: data – A list of at most three bytes
    Returns:Four base64 symbols (or ‘=’) corresponding to the data given in input
    Return type:str
    CU: len(octets) <= 3
    Examples:	
    >>> bytes_to_symbols([5])
    'BQ=='
    >>> bytes_to_symbols([4, 163])
    'BKM='
    >>> bytes_to_symbols([28, 89, 101])
    'HFll'
    >>> bytes_to_symbols([])
    ''
    """
    e2=0
    e3=0
    e4=0
    e1=0
    d=2
    i=0
    resultat=""
    if(len(octets)>0):
        while i<= (len(octets)-1):
            e1=(octets[i] >> d)
            e2=e4 | e1
            e3=e1 << d
            e4=(octets[i] ^ e3) << (6-d)
            i=i+1
            d=d+2
            resultat=resultat+BASE64_SYMBOLS[e2]
            
        resultat=resultat+ BASE64_SYMBOLS[e4]
        if((len(octets)*8)%6==4):
            resultat=resultat+"="
        elif((len(octets)*8)%6==2):
            resultat=resultat+"=="
            
    return resultat



#Question 5:
def base64_encode ( source ):
    """
    Encode a file in base64 and outputs the result on standard output .
    : param source : the source filename
    : type source : str
    """
    input=open(source,'rb')
    data = input.read(3)
    tligne=0
    nb = 0
    while len( data ) > 0:
        if(tligne%19==0):
            sys.stdout.write("\n")
        sys.stdout.write(str(bytes_to_symbols(data)))
        tligne=tligne+3
        data = input.read(3)
        
    
    input.close ();


#Question 7:
def decode_base64_symbol(symbol):
    """
    Convert a base64 symbol in integer.
    Parameters:	symbol (str) – the symbol to be converted
    Returns:the integer corresponding to the base64 symbol
    Return type:int
    CU:	the symbol is part of the base64 symbols
    Examples:	
    >>> decode_base64_symbol('A')
    0
    >>> decode_base64_symbol('Z')
    25
    >>> decode_base64_symbol('a')
    26
    >>> decode_base64_symbol('z')
    51
    >>> decode_base64_symbol('0')
    52
    >>> decode_base64_symbol('9')
    61
    >>> decode_base64_symbol('+')
    62
    >>> decode_base64_symbol('/')
    63
    >>> decode_base64_symbol('=')
    Traceback (most recent call last):
    ...
    AssertionError: decode_base64_symbol: the symbol is not part of base64
    """
    assert symbol!="=", "decode_base64_symbol: the symbol is not part of base64"
    inc=0
    for i in symbol:
        for b in BASE64_SYMBOLS:
            if(i==b):
                return inc
            inc=inc+1

#Question 8:           
def symbols_to_bytes(symbols):
    """
    Convert base64 symbols to bytes

    Parameters:	symbols (str) – a string of four base64 symbols (and maybe the = sign)
    Returns:	a list of one to 3 bytes whose values correspond to the base64 symbols
    Return type:	list
    CU:	len(symbols) == 4
    Examples:	
    >>> symbols_to_bytes('BQ==')
    [5]
    >>> symbols_to_bytes('BKM=')
    [4, 163]
    >>> symbols_to_bytes('HFll')
    [28, 89, 101]
    """
    resultat=[]
    nbegale=0
    tmp=0
    b=0
    d=4
    e=0
    for i in symbols:
        if(i=="="):
            nbegale=nbegale+1
    resultat.append(decode_base64_symbol(symbols[0]))        
    for i in range(1,len(symbols)-1-nbegale):
        resultat.append(decode_base64_symbol(symbols[i]))
        e=resultat[i] >> d
        resultat[i]=(e << d)^ resultat[i]
        resultat[i-1]=(resultat[i-1] <<(6-d))| e
            
        d=d-2
        tmp=i
    if(nbegale==2):
        b=decode_base64_symbol(symbols[tmp+1])
        b= b >> 4
        resultat[tmp]=resultat[tmp] << 2
        resultat[tmp]=resultat[tmp] | b
    elif(nbegale==1):
        b=decode_base64_symbol(symbols[tmp+1])
        b= b >> 2
        resultat[tmp]=resultat[tmp] << 4
        resultat[tmp]=resultat[tmp] | b
    elif(nbegale==0):
        b=decode_base64_symbol(symbols[tmp+1])
        resultat[tmp]=(resultat[tmp] << 6)| b
    return resultat

#Question 9:
def process_base64_line(line):
    """
    Process a line from a base64 input and writes the conversion on the output
    Parameters:	line (str) – a line of a base64 output
    CU:	len(line) % 4 == 0 and the line only contains base64 symbols (or possibly = signs)
    """
    i=4
    taille=len(line)
    tmp=[]
    a=[]
    
    
    if (taille%4==0):
        while(taille!=0):
            tmp.append(symbols_to_bytes(line[:4]))
            line=line[4:]
            for b in range(0,len(tmp[0])):
                a.append(tmp[0][b])
            taille=taille-4
            tmp.clear()
        
        for inc in a:
            sys.stdout.write(chr(inc))
        
#Question 10:
def base64_decode(source):
    """
    Decode a source file encoded in base64 and output the result.

    Parameters:	source (str) – the filename of the base64 file to decode
    """
    
    input=open(source,'r')
    data = input.read(76)   
    while len( data ) > 0:
        input.read(1)
        process_base64_line(data)
        data = input.read(76)
        
    input.close ();

    
if __name__ == "__main__":
    import doctest
    doctest.testmod()

    #Question 2:
    # auncun =: lorsque (8*nb_octets(nombre d'octet))%6==0
    #=: lorsque (8*nb_octets(nombre d'octet))%6==4
    #==: lorsque (8*nb_octets(nombre d'octet))%6==2

    #Question 3:
    print("Question 3: ")
    print(BASE64_SYMBOLS[5])
    print(BASE64_SYMBOLS[32])
    print(BASE64_SYMBOLS[45])

    #Question4:
    print("Question 4: ")
    print(bytes_to_symbols([1,2,3]))

    #Question 5:
    print("Question 5: ")
    base64_encode("./cigale1.txt")
    print()

    #Question 7:
    print("Question 7:")
    print(decode_base64_symbol("D"));

    #Question 8:
    print("Question 8:")
    print(symbols_to_bytes('HFll'))

    #Question 9:
    print("Question 9:")
    process_base64_line("TGEgQ2lnYWxl")
    print()
    
    #Question 10:
    print("Question 10:")
    base64_decode("./cigaletest.txt")
