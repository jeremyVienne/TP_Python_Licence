from time import sleep
def compte_a_rebours(x):

    while (x>=0):
        print(x)
        x=x-1
        sleep(1)
        

def somme_partielle(n):

    i=1
    somme=0
    while(i<=n):
        if(i%2==1):
            somme=somme-1/i
        elif(i%2==0):
            somme=somme+1/i
        i=i+1
    return somme

def imprimer_table(x):

    i=1
    while(i<=10):
        print(x," x ", i," = ", x*i)
        i=i+1
        

#for a in range(11)[1:]:
#    imprimer_table(a)


def u_terme(n):
    u0=0
    un=0
    unmoins=u0
    i=0
    if (n==0):
        return u0
    elif(n>=1):
        while(i<n):
            un=3*unmoins+1
            unmoins=un
            i=i+1
        return un
       
def atteint(M):
    i=0
    while (u_terme(i)<M):
        i=i+1
    i=i+1
    return i
