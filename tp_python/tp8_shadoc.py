Alphabet_Shadok = [GA,BU,ZO,MEU] = [chr(0x004F),chr(0x2212),chr(0x2A3C),chr(0x25FF)]

def entier_en_shadok(e):
    """
    >>> entier_en_shadok(2014)
    '−◿◿−◿⨼'
    """
    s=''
    while e:
        s=Alphabet_Shadok[e%4]+s
        e=e//4
    if s == '':
        s=GA
    return s

def shadok_en_entier(s):
    """
    >>> shadok_en_entier (GA)
    0
    >>> shadok_en_entier (BU)
    1
    >>> shadok_en_entier (ZO)
    2
    >>> shadok_en_entier (MEU)
    3
    >>> shadok_en_entier (MEU+BU)
    13
    """
    u=0
    for e in s:
        for (i,x) in enumerate(Alphabet_Shadok):
            if e == x:
                u = u*4+i
    return u

# tout nombre entier représentable sur un octect peut être écrit en shadok avec
# 4 chiffres shadoks car on divise se chiffre 4 fois par 4 ( soit 256/4/4/4/4 = 1 soit
# il est < 4, donc les 256 possibilité d'un octet est représentable avec un maximum de
# chiffres shadoks (2**8 = 4**4 )

def octet_en_shadok(o):
    """
    >>> octet_en_shadok (0)
    'OOOO'
    >>> octet_en_shadok (255)
    '◿◿◿◿'
    >>> octet_en_shadok (65)
    '−OO−'
    """
    r=''
    for i in (0,2,4,6):
        r=entier_en_shadok(o>>i&3)+r
    return r

def code_car_en_shadok(c):
    """
    >>> code_car_en_shadok ('A')
    '−OO−'
    >>> code_car_en_shadok ('e')
    '−⨼−−'
    """
    return octet_en_shadok(ord(c))

def code_en_shadok(s):
    """
    >>> code_en_shadok("Timoleon")
    '−−−O−⨼⨼−−⨼◿−−⨼◿◿−⨼◿O−⨼−−−⨼◿◿−⨼◿⨼'
    """
    retour=""
    for i in s:
        retour=retour+code_car_en_shadok(i)
    return retour

def decode_car_du_shadok(s):
    """
    >>> decode_car_du_shadok ('−OO−')
    'A'
    >>> decode_car_du_shadok ('O⨼⨼⨼')
    '*'
    """
    retour=0
    for i in s:
        retour=shadok_en_entier(i)+retour*4
    return chr(retour)

def decode_du_shadok(s):
    retour=''
    tmp=''
    for i in s:
        if (len(tmp)==4):
            retour=retour+decode_car_du_shadok (tmp)
            tmp=''
        else:
            tmp=tmp+i
    return retour















        
