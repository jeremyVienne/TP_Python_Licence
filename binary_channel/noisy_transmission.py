'''
   Simulating an information transmission through a noisy channel.
   
   :author: FIL - IEEA - Univ. Lille 1 (déc. 2010, août 2015)
'''

import sys
import binary_channel

def transmit(p, encode, in_filename, out_filename):
    '''
    Read bytes in the input, process them using the `encode` function,
    send them through a CBSSM (whose error probability is `p`) and finally
    write them in the output.

    :param p: Error probability
    :type p: float
    :param encode: A function that takes a byte in parameter and returns a list of bytes.
    :type encode: function
    :param in_filename: Input filename
    :type in_filename: str
    :param out_filename: Output filename
    :type out_filename: str
    :UC: 0 <= p <= 1
    '''
    try:
        
        stream=open(in_filename,'rb')
        out_file=open(out_filename,'wb')
        
        
        value=stream.read(1)[0]
        while(value!=""):
            enc=encode(value)
            for i in enc:
                out_file.write(bytes([binary_channel.cbssm(p,i)]))
            value=stream.read(1)[0]
            
        stream.close()
        out_file.close()
    except:
        return None

    
    
def put_byte_in_list(byte):
    '''
    Put a byte in a list of one element.

    :param byte: A byte
    :type byte: int
    :return: A list of one element: `byte`
    :rtype: list
    :Examples:

    >>> put_byte_in_list(120)
    [120]
    >>> put_byte_in_list(64)
    [64]
    '''

    return [byte]

def receive(nb_bytes, decode, in_filename, out_filename):
    '''
    Decode a file transmitted with an error-correction code.
    The error-correction used must encode one or several bytes at the same time.
    
    The function reads bytes in the input, process them using the `decode`
    function, and finally write them in the output.

    :param nb_bytes: The number of bytes to read so that one byte is decoded.
    :type nb_bytes: int
    :param decode: A function that takes a `bytes` object (containing `nb_bytes` bytes) in parameter and returns a byte
    :type decode: function
    :param in_filename: Input filename
    :type in_filename: str
    :param out_filename: Output filename
    :type out_filename: str
    :return: The number of detected errors and the number of corrected errors
    :rtype: tuple
    :UC: nb_bytes > 0
    '''

    stream=open(in_filename, 'rb')
    out_file=open(out_filename,'wb')

    value=stream.read(nb_bytes)
    byte=0
    error=0
    corr=0
    e=0
    c=0
    while(value!="" and len(value)==3):
        
        byte,e,c=decode(bytes([value[0],value[1],value[2]]))
        error+=e
        corr+=c
        out_file.write(bytes([byte]))
        value=stream.read(nb_bytes)
    return "Nombre d'erreur: "+ str(error) + ", nombre de correction: "+str(corr)
def usage ():
    '''
    `usage ()` indicates how to use the program
    '''
    print( "Usage : %s <p> <input> <output>" % sys.argv[0]);
    print( "\t<p> = error probability (on one bit)") ;
    print( "\t<input> = filename corresponding to the CBSSM input") ;
    print( "\t<output> = filename corresponding to the CBSSM output") ;
    exit(1)


def main ():
    if len(sys.argv) != 4:
        usage ()
    else:
        p = float(sys.argv[1])
        in_filename = sys.argv[2]
        out_filename = sys.argv[3]
        transmit(p, put_byte_in_list, in_filename, out_filename)
        exit(0)

if __name__ == '__main__':
    main()
