'''
Implantation de l'algorithme de Huffman

@author FIL - IEEA - Univ. Lille (août 2015)
'''

import doctest
import operator
from huffman_tree import HuffmanTree
import coding
import struct
import tpcodings

def symbol_occurrences(stream):
    '''
    Read the stream and count the occurrences of each symbol in the stream
    
    :param stream: a stream opened (in read mode and (possibly) in binary mode)
    :return: A dictionary whose keys are symbols and the associated values are\
    the corresponding number of occurrences
    :rtype: dict
    :Examples:
    
    >>> from io import StringIO # StringIO is used to have stream examples based on strings.
    >>> from io import BytesIO # BytesIO is used to have stream examples based on bytes.
    >>> symbol_occurrences(StringIO("ababcaba")) == {'c': 1, 'b': 3, 'a': 4}
    True
    >>> symbol_occurrences(BytesIO(b"ababcaba")) == {b'c': 1, b'b': 3, b'a': 4}
    True
    >>> symbol_occurrences(StringIO('aaaa')) == {'a': 4}
    True
    >>> symbol_occurrences(StringIO(''))
    {}
    >>> symbol_occurrences(StringIO('abcd')) == {'a': 1, 'b': 1, 'c': 1, 'd': 1}
    True
    >>> symbol_occurrences(BytesIO(b'abcd')) == {b'a': 1, b'b': 1, b'c': 1, b'd': 1}
    True
    '''
    counters={}

    ns=""
    inc=0
    while(stream.read(1)):
        stream.seek(inc)
        ns=stream.read(1)
        if (ns in counters):
            counters[ns]+=1
        else:
            counters[ns]=1
        inc+=1
    return counters

def create_forest(occurrences):
    '''
    Create the initial list of Huffman trees based on the dictionary of
    symbols given in parameter.
    
    :param occurrences: Number of occurrences of each symbol.
    :type occurrences: dict
    :return: A list sorted in ascending order on the number of occurrences\
    and on the symbols of Huffman trees of all symbols provided in\
    `occurrences`.
    :Examples: 

    >>> create_forest({'a': 4, 'c': 2, 'b': 1})
    [|b:1|, |c:2|, |a:4|]
    >>> create_forest({'e': 1, 'f': 1, 'g': 1, 'h': 1, 'a':2})
    [|e:1|, |f:1|, |g:1|, |h:1|, |a:2|]
    '''
    sorted_occs = sorted(occurrences.items(), key=lambda item: (item[1], item[0]))
    forest = [HuffmanTree(chr(leaf[0][0]),leaf[1]) for leaf in sorted_occs]
    return forest

def pop_least_element(list1, list2):
    '''
    Get and remove the lowest element from two lists sorted in ascending order.

    :param list1: First list sorted in ascending order
    :type list1: list
    :param list2: Second list sorted in ascending order
    :type list2: list
    :return: The lowest element among the two lists
    :UC: The two lists are sorted in ascending order and there is at least\
    one element among the two lists.
    :Examples:

    >>> pop_least_element([1], [2])
    1
    >>> pop_least_element([2], [1])
    1
    >>> pop_least_element([], [1])
    1
    >>> pop_least_element( [1], [])
    1
    '''
    assert(len(list1) + len(list2) >= 1)
    if len(list1) == 0:
        return list2.pop(0)
    if len(list2) == 0:
        return list1.pop(0)
    if list2[0] < list1[0]:
        return list2.pop(0)
    return list1.pop(0)

def create_huffman_tree(occurrences):
    '''
    Return a Huffman tree of the symbols given in `occurrences`.
    
    :param occurrences: Number of occurrences of each symbol.
    :type occurrences: dict
    :return: Return a single Huffman tree (obtained with Huffman algorithm)\
    of the symbols in `occurrences`.
    :rtype: huffman_tree.HuffmanTre
    :Examples:
    
    >>> create_huffman_tree({'a': 4, 'b': 1, 'c': 2})
    |bca:7|_<|bc:3|_<|b:1|, |c:2|>, |a:4|>
    >>> create_huffman_tree({'a': 1, 'b': 1, 'c': 2})
    |cab:4|_<|c:2|, |ab:2|_<|a:1|, |b:1|>>
    '''
    symbol_list = create_forest(occurrences)
    tree_list = []
    #symbol_list-> ce qu'il reste à traiter
    #tree_list -> resultat + opérations
    while len(tree_list) + len(symbol_list) != 1:
        (elem1, elem2) = (pop_least_element(symbol_list, tree_list),\
                          pop_least_element(symbol_list, tree_list))
        new_tree = HuffmanTree(left = elem1, right=elem2)
        tree_list.append(new_tree)

    
    
    if len(tree_list) == 1:
        
        return tree_list[0]
    
    print(tree_list)
    return symbol_list[0]

def get_coding_from_tree(tree, code=''):
    '''
    Get the codes associated to the symbols.

    :param tree: A HuffmanTree
    :type tree: huffman_tree.HuffmanTree
    :param code: (optional parameter) the path that was followed to access the\
    current root of the tree
    :return: a list of tuples. Each tuple is made of a symbol and a code.\
    The order of the tuples in the list does not matter
    :rtype: list
    :Examples:

    >>> c=get_coding_from_tree(create_huffman_tree({'a': 4, 'b': 1, 'c': 2}))
    >>> len(c)
    3
    >>> c.count(('a', '1')) == 1
    True
    >>> c.count(('b', '00')) == 1
    True
    >>> c.count(('c', '01')) == 1
    True
    '''
    if tree.isLeaf():
        return [(tree.symbol, code)]
    return get_coding_from_tree(tree.left, code + '0') \
        + get_coding_from_tree(tree.right, code + '1')
    
def huffman_coding(tree):
    '''
    Creates a Huffman coding from a Huffman tree.

    :param tree: A Huffman tree
    :type tree: huffman_tree.HuffmanTree
    :return: A Huffman coding based on the Huffman tree given in parameter
    :rtype: coding.Coding
    :Examples:

    >>> c = huffman_coding(create_huffman_tree({'a': 4, 'b': 1, 'c': 2}))
    >>> c.code('a') + ' ' + c.code('b') + ' ' + c.code('c')
    '1 00 01'
    >>> c = huffman_coding(create_huffman_tree({'a': 1, 'b': 2, 'c': 3, 'd': 5}))
    >>> c.code('a') + ' ' + c.code('b') + ' ' + c.code('c') + ' '\
    + c.code('d')
    '110 111 10 0'
    '''
    result = get_coding_from_tree(tree, '')
    alphabet = list(map(lambda i: i[0], result))
    codes = list(map(lambda i: i[1], result))
    return coding.create(alphabet, codes)

def write_occurrences(occurrences, filename):
    '''
    Write the symbol occurrences in the given file
    
    :param occurrences: The dictionary of symbol occurrences
    :type occurrences: dict
    :param filename: The filename where the occurrences must be written.
    :type filename: str
    '''
    
    stream = open(filename, 'wb')
    for i in occurrences:
        stream.write(bytes(struct.pack('i',ord(i))))
        stream.write(bytes(struct.pack('i',occurrences[i])))
        
    stream.close() 
        
def read_occurrences(filename):
    '''
    Read the symbol occurrences from the given file.

    :param filename: The filename where the occurrences must be read.
    :type filename: str
    :return: A dictionary of the symbol occurrences
    :rtype: dict
    :Examples:

    >>> import tempfile; temp = tempfile.NamedTemporaryFile()
    >>> d = {b'c': 1, b'b': 3, b'a': 4}
    >>> write_occurrences(d, temp.name)
    >>> read_occurrences(temp.name) == d
    True
    >>> d = {b'e': 1, b'f': 1, b'g': 1, b'h': 1, b'a':2}
    >>> write_occurrences(d, temp.name)
    >>> read_occurrences(temp.name) == d
    True
    '''

    stream=open(filename,'rb')
    d=dict()

    tmp=False
    inc=0
    value=""
    save=""
    while(stream.read(struct.calcsize('i'))):
        stream.seek(inc)
        value=stream.read(struct.calcsize('i'))
        if(tmp==False):
            d[bytes([struct.unpack('i',value)[0]])]=0
            save=bytes([struct.unpack('i',value)[0]])
            tmp=True
        else:
            tmp=False
            d[save]=struct.unpack('i',value)[0]
        inc+=struct.calcsize('i')
    stream.close()
    return d
            
    
def huffman_encode(filename, out_filename):
    '''
    Encode a file using Huffman algorithm and writes the result to 
    an other file.
    
    Two files will be created. One called `out_filename` containing
    a Huffman encoding of the input file. Another one called
    `out_filename`+".code" which will contain the occurrences of each 
    symbol.

    :param filename: The filename of the file to be encoded.
    :type filename: str
    :param out_filename: The filename of the file where the resulting\
    encoding will be stored.
    :type out_filename: str
    '''
    stream = open(filename, 'rb')
    # Calcul du nombre d'occurrences
    occ=symbol_occurrences(stream)
    # Création du codage de Huffman
    codHuff=create_huffman_tree(occ)
    # Ecriture du fichier stockant le dictionnaire d'occurrences
    write_occurrences(occ,out_filename+".code")
    # Mise de la tête de lecture au début du fichier pour le reparcourir
    c=huffman_coding(codHuff)

    
    value=""
    inc=0
    stream.seek(0)
    v=""
    while(stream.read(1)):
        stream.seek(inc)
        value=stream.read(1)[0]
        v=v+c.code(chr(value))
        #dest.write(bytes(struct.pack('i',int(c.code(chr(value[0])),2))))
        inc+=1
    tpcodings.write_binary_string_in_file(v,out_filename)  
    # Parcours du fichier et encodage des symboles lus
    stream.close()
    
    

def prefix_tree_decoding(bits, tree):
    '''
    Return the decoding of the binary string given in parameter
    using the Huffman tree `tree`.
    
    :param bits: a binary string (only made of 0s and 1s)
    :type bits: str
    :param tree: a Huffman tree
    :type tree: huffman_tree.HuffmanTree
    :return: Return the concatenation of symbols represented by the binary string.\
    The binary string is decoded using the Huffman tree.
    :rtype: bytes
    :UC: The binary string must end in a leaf.
    :Examples:

    >>> tree = create_huffman_tree({b'a': 1, b'b': 2, b'c': 3, b'd': 5})
    >>> prefix_tree_decoding('111110100111111110', tree)
    b'bacdbba'
    '''
    noeud = tree
    sortie = ''
    for bit in bits:
        if noeud.isLeaf():
            sortie += noeud.symbol
            noeud = tree
        if bit == '0':
            noeud = noeud.left
        else:
            noeud = noeud.right
    assert(noeud.isLeaf()), "La chaine devrait se terminer sur une feuille"
    sortie += noeud.symbol
    return sortie
    
def huffman_decode(filename, out_filename):
    '''
    Decode a file encoded with a Huffman encoding.

    :param filename: the file name of the Huffman encoded file
    :type filename: str
    :param out_filename: the file name where the decoding will be stored
    :type out_filename: str
    '''
    value=tpcodings.read_file(filename)
    occ=read_occurrences(filename+".code")
    
    codHuff=create_huffman_tree(occ)
    c=huffman_coding(codHuff)
    s=""
    
    s=prefix_tree_decoding(value,codHuff)
    
    stream=open(out_filename,'wb')

    for e in s:
        stream.write(bytes([ord(e)]))
    stream.close()
