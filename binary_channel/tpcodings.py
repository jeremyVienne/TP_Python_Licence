#!/usr/bin/env python3

#sys.stdout.buffer.write(<bytes>)

from coding import *
from TP2 import *

source_alphabet = \
['A','B','C','D','E','F','G','H','I','J','K','L','M','N',\
'O','P','Q','R','S','T','U','V','W','X','Y','Z',' ']

code1=\
["00000","00001","00010","00011","00100","00101","00110","00111","01000","01001","01010","01011","01100","01101","01110","01111",
"10000","10001","10010","10011","10100","10101","10110","10111",
"11000","11001","11111"]


code2=\
[".-/","-.../","-.-./","-../","./","..-./","--./","..../","../",
".---/","-.-/",".-../","--/","-./","---/",".--./","--.-/",".-./",
".../","-/","..-/","...-/",".--/","-..-/","-.--/","--../","---./"]

code3=\
["1010","0010011","01001","01110","110","0111100","0111110",
"0010010","1000","011111110","011111111001","0001","00101",
"1001","0000","01000","0111101","0101","1011","0110","0011",
"001000","011111111000","01111110","0111111111","01111111101",
"111"]


coding1 = create(source_alphabet,code1)
coding2= create(source_alphabet, code2)
coding3= create(source_alphabet, code3)

# Question 8 code chaine de caractère avec le codage passé en paramètre
def code_word(mot,codage):
    """
    Code a word with the provided coding

    Parameters:	 mot (str) – the word to be coded
    codage (Coding) – the coding to use for coding the word
    Returns: word coded with my_coding
    Return type: str
    CU:	Symbols in the word are in the source alphabet of the coding
    Examples:	
    >>> code_word('',coding1)
    ''
    >>> code_word('ABCD',coding1)
    '00000000010001000011'
    >>> code_word(' ZA',coding1)
    '111111100100000'
    """
    liste= list(mot)
    resultat=""
    for i in liste:
        resultat += codage.code(i)
    return resultat

def decode_fixed_length_word(codeword, my_coding):
    """
    Decode a word using a fixed-length coding

    Parameters:	
    codeword (str) – the codeword to be decoded
    my_coding (Coding) – the coding to use for decoding the codeword
    Returns:	
    the result of decoding codeword with my_coding
    Return type:	
    str
    CU:	
    The codeword was obtained from the coding my_coding
    Examples:	
    >>> decode_fixed_length_word('', coding1)
    ''
    >>> decode_fixed_length_word('111111100100000', coding1)
    ' ZA'
    >>> decode_fixed_length_word(code_word(''.join(source_alphabet), coding1), coding1)
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ '
    >>> decode_fixed_length_word('11111110010000', coding1)
    Traceback (most recent call last):
    ...
    coding.Undecodable_word: decode_fixed_length_word: undecodable word
    >>> decode_fixed_length_word('1   22', coding1)
    Traceback (most recent call last):
    ...
    coding.Undecodable_word: decode_fixed_length_word: undecodable word
    """
    
     
    try :
        l = len(my_coding.code(my_coding.alphabet()[0]))
        if(len(codeword)%l!=0):
            raise Undecodable_word("decode_fixed_length_word: undecodable word")
            

        #tmp=list(codeword[i*l:(i+1)*l] for i in range (len(codeword)//l) )
        tmp=list(codeword[i*l:(i+1)*l] for i in range (len(codeword)//l ) )
        retour=""
        for e in tmp:
            retour+= my_coding.decode(e)
        return retour
    except:
        raise Undecodable_word("decode_fixed_length_word: undecodable word")        

def decode_comma_word(word, comma, my_coding):
    """
    Code a word with the provided comma coding

    Parameters:	
    word (str) – the word to be coded
    comma (str) – the symbol used as a separator
    my_coding (Coding) – the coding to use for coding the word
    Returns:	
    word decoded with my_coding
    Return type:	
    str
    CU:	
    len(comma) == 1 and Symbols in the word are in the source alphabet of the coding
    Examples:	
    >>> decode_comma_word('', '/', coding2)
    ''
    >>> decode_comma_word(code_word(''.join(source_alphabet), coding2), '/', coding2)
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ '
    >>> decode_comma_word('-.../-.-', '/', coding2)
    Traceback (most recent call last):
    ...
    coding.Undecodable_word: decode_comma_word: comma not found, cannot decode the word
    """
    try:
        tmp=list()
        retour=""
        
        while ( len ( word ) > 0 ) :
            if ( word.find(comma) != -1 ):
                tmp.append(word[:word.find(comma)+1])
                word=word[word.find(comma)+1:]
            else:
                raise Undecodable_word("decode_comma_word: comma not found, cannot decode the word")
        for i in tmp:
            retour += my_coding.decode(i)
        return retour
    except:
        raise Undecodable_word("decode_comma_word: comma not found, cannot decode the word")

    
def decode_prefix_letter ( word , my_coding ):
    """
    Decodes the first letter of the word , assuming a prefix coding was used .
    : param word : A word that was coded using ‘ coding ‘
    : type word : str
    : param my_coding : The coding used for ( de ) coding
    1. Cette méthode n'est pas la plus efficace. Il est préférable d'utiliser une représentation arborescente du codage,
    comme il a été vu en cours. Cela fera l'objet d'un prochain TP.
    6
    : type my_coding : coding . Coding
    : return : a tuple whose elements are : 1) the symbol associated with the \
    first decodable prefix 2) the length of the first decodable prefix
    : rtype : tuple
    : CU : ‘ word ‘ was coded using ‘ my_coding ‘
    : Examples :
    >>> decode_prefix_letter ("0010010" , coding3 )
    ('H', 7)
    >>> decode_prefix_letter ("00100101000" , coding3 )
    ('H', 7)
    >>> decode_prefix_letter ("00" , coding3 )
    Traceback (most recent call last):
    ...
    coding.Undecodable_word: decode_prefix_letter : no decodable prefix
    """
    word_length = len ( word )
    for i in range (1 , word_length +1):
        try :
            prefix = my_coding.decode ( word [: i ])
            return ( prefix , i )
        except :
            pass
    raise Undecodable_word ("decode_prefix_letter : no decodable prefix")

def decode_prefix_word (word, my_coding):
    """
    Parameters:	
    word (str) – the word to be decoded
    my_coding (Coding) – the prefix coding that was used for coding the word
    Returns:	
    word decoded with my_coding
    Return type:	
    str
    CU:	
    The word was coded using the coding my_coding
    Examples:	
    >>> decode_prefix_word("0010010", coding3)
    'H'
    >>> decode_prefix_word("00100101000", coding3)
    'HI'
    >>> decode_prefix_word("00", coding3)   
    Traceback (most recent call last):
    ...
    coding.Undecodable_word
    >>> decode_prefix_word(code_word(''.join(source_alphabet), coding3), coding3)
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ '
    """
    try :
        word_len=len(word)
        retour = ""
        while ( len(word) > 0 ):
            retour = retour + decode_prefix_letter(word,my_coding)[0]
            word=word[decode_prefix_letter(word,my_coding)[1]:]
        return retour
    except:
        raise Undecodable_word()

def write_bits(stream,bits):
    """
    Parameters:	
    stream – a steam opened in write and binary modes
    bits (str) – a string made of binary characters
    Action:	
    Writes all the possible bits to the stream. We recall that bits can only be written byte per byte (8 bits per 8 bits).
    Returns:	
    the bits that have not been written yet to the stream.
    Examples:	
    >>> # Next line creates a temporary file for tests
    >>> import tempfile; r=tempfile.NamedTemporaryFile()
    >>> write_bits(r, '11011111')
    ''
    >>> write_bits(r, '110')
    '110'
    >>> write_bits(r, '11011111000000010110')
    '0110'
    >>> r.seek(0) # Go back at the start of the file
    0
    >>> list(r.read()) # Read the three bytes that should have been written to the file
    [223, 223, 1]
    >>> write_bits(tempfile.NamedTemporaryFile(mode='w'), '11011111000000010110')
    Traceback (most recent call last):
    ...
    AssertionError: The stream must be opened in write and binary modes ('wb')
    """
    assert 'b' in stream.mode,"The stream must be opened in write and binary modes ('wb')"
    while(len(bits)>=8):
        tmp=list()
        tmp.append(binary_str_to_integer ( bits[:8] ))
        stream.write ( bytes ( tmp[:] ) )
        tmp=list()
        bits=bits[8:]
    return bits

def read_bits(stream):
    """
    Parameters:	stream – The input stream which was opened in read and binary modes.
    Returns:	A binary string made of 8 bits (or an empty string)
    Return type:str
    CU:	The stream was opened in read and binary modes.
    Examples:	
    >>> # Create a temporary file
    >>> import tempfile; r=tempfile.NamedTemporaryFile(); 
    >>> write_bits(r, '1101111100000001') # Write data into the file
    ''
    >>> r.seek(0) # Go back at the start of the file
    0
    >>> read_bits(r) # Read the first 8 bits
    '11011111'
    >>> read_bits(r) # Read the following 8 bits
    '00000001'
    >>> read_bits(r) # The end of the file is reached
    ''
    """
    assert 'rb' in stream.mode
    try:
        resultat='{:b}'.format(stream.read(1)[0])
        while (len(resultat) <8):
            resultat="0"+resultat       
        return resultat
    except:
        return ''
    


    
def complete_byte(bits):
    """
    Parameters:	bits (str) – a binary string
    Returns:	A binary string of 8 bits which completes the string bits. The completion adds a 1 followed by as many zeroes as necessary to reach 8 bits.
    Return type:	str
    CU:	len(bits) < 8
    Examples:	
    >>> complete_byte('01')
    '01100000'
    >>> complete_byte('0100001')
    '01000011'
    >>> complete_byte('')
    '10000000'
    >>> complete_byte('00000001')
    Traceback (most recent call last):
    ...
    AssertionError: I cannot complete a completed byte!
    """
    assert len(bits)<8, "I cannot complete a completed byte!"

    bits=bits+"1"
    while ( len ( bits ) < 8 ):
        bits+="0"
    return bits

def uncomplete_byte(bits):
    """
    Parameters:	bits – a string of 8 bits
    Returns:	A binary string of length < 8 for which the completion was removed (from the last 1-bit to the end).
    Return type:	str
    CU:	len(bits) == 8 and the byte must have at least one 1-bit.
    Examples:	
    >>> uncomplete_byte('01100000')
    '01'
    >>> uncomplete_byte('01000011')
    '0100001'
    >>> uncomplete_byte('10000000')
    ''
    >>> uncomplete_byte('0000000')
    Traceback (most recent call last):
    ...
    AssertionError: I can only uncomplete a byte
    """
    assert '10' in bits, 'I can only uncomplete a byte'
    return bits[:bits.rfind('1')]

def remove_completion(bits):
    """
    Parameters:	bits (str) – a binary string of length >= 8 (which was already completed)
    Returns:	Return the binary string where the completion has been removed at the end (please note that the completion is done only on the last byte).
    Return type:	str
    CU:	len(bits) >= 8
    Examples:	
    >>> remove_completion('1010101010000000')
    '10101010'
    >>> remove_completion('1010101001100000')
    '1010101001'
    """
    assert len(bits)%8==0, "len(bits) multiple de 8"
    resultat=""
    resultat=bits[:(len(bits)-8)]+uncomplete_byte(bits[(len(bits)-8):])
    return resultat

def flush_binary_string ( binary , stream ):
    8
    '''
    Flush a binary string by writing as many bytes as possible in the output
    stream .
    : param binary : A binary string
    : type binary : str
    : param stream : An output stream
    : return : the bits that could not be written in the output stream ( the \
    length of the returned string is necessarily < 8).
    : Examples :
    >>> import tempfile ; r = tempfile . NamedTemporaryFile ()
    >>> flush_binary_string ( '01000001 ' , r )
    ''
    >>> r . seek (0);
    0
    >>> r . read (). decode ()
    'A'
    '''
    while len ( binary ) >= 8:
        binary = write_bits ( stream , binary )
    return binary

def write_binary_string_in_file ( binary , file ):
    '''
    Write the binary string in the file ( the string is written 8 bits per 8
    bits in the file ).
    As the binary string can have any length , the last byte will be completed
    so that all the content could be written to the file .
    : param binary : a binary string
    : type binary : str
    : param file : The filename of the file where the binary string will be \
    written
    : type file : str
    : Examples :
    >>> import tempfile ; r =tempfile.NamedTemporaryFile()
    >>> write_binary_string_in_file ('01000001010',r.name)
    >>> r . seek (0);
    0
    >>> r.read().decode ()
    'AP'
    '''
    out_file = open (file , 'wb')
    binary = flush_binary_string ( binary , out_file )
    write_bits ( out_file , complete_byte ( binary ))
    out_file . close ()
    
def read_file ( file ):
    '''
    Read the data in the file and returns a binary string corresponding to
    that data .
    : param file : the filanem of the file to read .
    : type file : str
    : return : The binary string of the data that was stored in the file . The \
    completion will be removed from the binary string .
    : rtype : str
    : Examples :
    >>> import tempfile ; r = tempfile . NamedTemporaryFile ()
    >>> write_binary_string_in_file ( '01000001010 ' , r . name )
    >>> r . seek (0);
    0
    >>> read_file ( r . name )
    '01000001010'
    '''
    in_file = open (file ,'rb')
    bits = ''
    binaire = read_bits ( in_file )
    while binaire != '':
        bits += binaire
        binaire = read_bits ( in_file )
    in_file . close
    if len ( bits ) > 0:
        bits = remove_completion ( bits )
    return bits    
                                
    

     
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()

    # Partie 1

##    source_alphabet = ['a', 'b', 'c']
##    code = ['010 ', '100 ', '110 ']
##    my_coding = create(source_alphabet,code)

    #code
##    print("a: ", my_coding.code(source_alphabet[0]))
##    print("b: ", my_coding.code(source_alphabet[1]))
##    print("c: ", my_coding.code(source_alphabet[2]))

    #decode
##    print("010: ", my_coding.decode(code[0]))
##    print("100: ", my_coding.decode(code[1]))
##    print("110: ", my_coding.decode(code[2]))

    # print(my_coding.code('j')) -> coding.Not_codable_symbol

    # print(my_coding.decode('111'))  -> coding.Undecodable_word

    # Partie 2
    
   

    #code question 7
##    print("coding1 A: ",coding1.code(source_alphabet[0]))
##    print("coding2 A: ", coding2.code(source_alphabet[0]))
##    print("coding3 A: ", coding3.code(source_alphabet[0]))

    # decode question 7
##    print("decode 00000: ", coding1.decode(code1[0]))
##    print("decode . -/: ", coding2.decode(code2[0]))
##    print("decode 1010: ", coding3.decode(code3[0]))

    # Code Question 8
##    print("coding1 CODAGE: ",code_word("CODAGE", coding1))
##    print("coding2 CODAGE: ",code_word("CODAGE", coding2))
##    print("coding3 CODAGE: ",code_word("CODAGE", coding3))

    #Question 12
    #print("coding1 CODAGE: ",decode_fixed_length_word("000100111000011000000011000100", coding1))
    #print("coding2 CODAGE: ",decode_fixed_length_word("-.-./---/-../.-/--././ ", coding2))

    #Question 13
    #print(decode_fixed_length_word("0101100000111110111100111010000101100000011011001100111100010111001111010000010011111000110010011111010111111101110101001010110001010000010010001111110001000111000001000101111001000110110011010000010010001", coding1))

    t=".--./---/..-/.-./---./.-../.-/--\
-./..-./.-./.-/-./-.-././---./-.\
./---././-./---./-.../.-/.../---\
./-.././.../---./-./---/..-/../.\
-../.-.././.../---././-./-.-./--\
-/.-././"
    #print(decode_comma_word(t, "/", coding2) ) #POUR LA FRANCE D EN BAS DES NOUILLES ENCORE

    text = "01100010010101000011101011111110\
10110110111011000000011011111110\
00000011010110111111010111011110\
0101010000101110"
    #print(decode_prefix_word ( text , coding3 ) ) #THALES EST TOUJOURS A FAIRE

    #f=open('file.txt','wb')
##    f.write(bytes([65,66]))
##    f.close() #ecrit 'AB' dans le fichier file
    #print(write_bits(f,'11110000110')) #110

    #print(uncomplete_byte('01100000'))
    #print(remove_completion('1010101001100000'))

    
    chaine='01100010010101000011101011111110\
10110110111011000000011011111110\
00000011010110111111010111011110\
0101010000101110' #mot3 en binaire
    write_binary_string_in_file(chaine, 'mot3.data.txt')
    #taille du fichier mot3.data: 1ko
    #mot3=bT:þ¶ìþ[õÞT.€

    #print(read_file('mot3.data.txt'))
    #print(read_file('mot3.data.txt')==chaine) #True






















    
