from turtle import *

def dessiner(seq=['F', '-', '-', 'F', '-', '-', 'F', '-', '-'],l=100,a=60):
    seq = seq[::-1]
    while (len(seq)>0):
        mot=seq.pop()
        if (mot=="F"):
            forward(l)
        elif(mot=="+"):
            left(a)
        elif(mot=="-"):
            right(a)


def derive(so=['F', '+', 'F'],r=['F', '-', 'F']):
    """
    Examples:
    >>> derive()
    ['F', '-', 'F', '+', 'F', '-', 'F']
    """
    retour=[]
    for inc in so:
        if (inc =="F"):
            for i in r:
                retour.append(i)
        else:
            retour.append(inc)
    return retour


    
def derive_n(n=2,so=['F', '+', 'F'],r=['F', '-', 'F']):
    """
    Examples:
    >>> derive_n(0)
    ['F', '+', 'F']
    >>> derive_n(1)
    ['F', '-', 'F','+', 'F', '-', 'F']
    >>> derive_n()
    ['F', '-', 'F', '-', 'F', '-', 'F','+', 'F', '-', 'F', '-', 'F', '-', 'F']
    """
    retour=so
    for inc in range(n):
        retour=derive(retour,r)
    return retour

if __name__=="__main__":
    import doctest
    doctest.testmod()

    
    #dessiner(['F', '-', '-', 'F', '-', '-', 'F', '-', '-'])
    #dessiner(['F','+','F','+','F','+','F','+'],100,90)
    
    #print (derive())

    #print(derive_n())

    
    speed(0)

    goto(0,0)

    for n in (0,4):
        l=3**(5-n)
        a=60
        liste=derive_n(n,['F','-','-','F','-','-','F','-','-'],['F','+','F','-','-','F','+','F'])
        #dessiner(liste,l,a)
        #a=90
        #liste=derive_n(n,['F'],['F', '+', 'F', '-', 'F', '-', 'F', '+', 'F'])
        dessiner(liste,l,a)
        left(90)
        dessiner(liste,l,a)
        left(90)
        dessiner(liste,l,a)
        left(90)
        dessiner(liste,l,a)


    


