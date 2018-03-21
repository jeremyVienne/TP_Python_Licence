from random import randint


def plus_ou_moins():
    
    imin=int(input("Intervalle min: "))
    imax=int(input("Intervalle max: "))
    nb=int(input("Nombres d'essais: "))


    
    mystere=randint(imin,imax)
    print("Rentrez un chiffre: ")
    x=int(input())
    
    while(x!=mystere and i<=nb):
        print((nb)-i," essais restant")
        x=int(input())
        if(x<mystere):
            print("Plus")
        elif(x>mystere):
            print("Moins")
        i=i+1
    if(x==mystere):
        print ("Nombre d'essais: ", i)
        print("Gagné")
    elif(i>7):
        print("Perdu")
