#!/usr/bin/env python3
# Lecornet Didrick
# Vienne Jeremy


from turtle import *
from random import randint
from math import floor

speed(0)

penup()
goto(-50,0)
pendown()

def carre(a=50):
    for i in range(4):
        forward(a)
        left(90)

def carres_alignes():
    for i in range(1,11):
            carre()
            penup()
            forward(55)
            pendown()
            
def cent_carres():
    for b in range(1,11):
        carres_alignes()
        penup()
        left(180)
        forward(550)
        left(-90)
        forward(55)
        left(-90)
        pendown()
        
def carres_emboites(a=50): # a = nombre de carrés
    for i in range(1,a+1):
        carre(10+(10*(i-1)))
        penup()
        goto(-200,-200)
        pendown()

def carres_tournant(a=7): # a = nombre de carrés
    for i in range(1,a+1):
        carre(300)
        left(360/a)

def polygones_convexes(n=4,l=100): # n = nombre cotés, l = longueur coté
    for i in range(1,n+1):
        forward(l)
        left(360/n)

def quatre_polygones_reguliers():
    pos=[-200,200,200,-200,-200]
    for i in range(4):
        penup()
        goto(pos[i],pos[i+1])
        pendown()
        polygones_convexes(i+4)
        
def polygone_etoile(n=5,l=500):  #polygone_etoile avec n et l, pas compris l'utilisation de "k", marche quand meme
    for i in range(1,n+2):
        forward(l)
        if (n%2==False):
            right(180-(360/(n)))
        else:
            right(180-(180/(n)))
            
def quatre_polygones_etoiles():
    pos=[-200,200,200,-200,-200]
    n=[5,7,8,9]

    for i in range(4):
        penup()
        goto(pos[i],pos[i+1])
        pendown()
        polygone_etoile(n[i],100)


def tortue_sortie(cote_carre):
    if ( xcor() > cote_carre/2 or xcor() < -cote_carre/2 or ycor() > cote_carre/2 or ycor() < -cote_carre/2 ):
        return True
    else:
        return False

def random():
    cote_carre=400
    n=cote_carre/2
    inc=0
    
    penup()
    goto(-cote_carre/2,-cote_carre/2)
    pendown()
    carre(cote_carre)
    penup()
    goto(0,0)
    pendown()

    while(tortue_sortie(cote_carre)==False and inc < n):
        forward(randint(10,30))
        left(randint(0,359))
        if ( tortue_sortie(cote_carre) ):
            pencolor("red")
        else:
            pencolor("green")
        inc = inc + 1
    return tortue_sortie(cote_carre)


def Billard(dimx=400,dimy=300,positionx=0,positiony=0,direction=randint(0,359),rebond=200):

    penup()
    goto(-dimx/2,-dimy/2)
    begin_fill()
    fillcolor("green")
    pendown()
    forward(dimx)
    left(90)
    forward(dimy)
    left(90)
    forward(dimx)
    left(90)
    forward(dimy)
    left(90)
    penup()
    goto(positionx,positiony)
    pendown()

    end_fill()
    
    left(direction)
    
    inc=0
    while(inc<rebond):
        forward(1)
        if( xcor() > dimx/2 or xcor() < -dimx/2 or ycor() > dimy/2 or ycor() < -dimy/2):
            if(xcor()>dimx/2 or xcor()<-dimx/2):
                left(180-2*heading())
            elif(ycor()>dimy/2 or ycor()<-dimy/2):
                left(180-2*heading()-180)
            inc=inc+1
            # pencolor(randint(0,255)/255,randint(0,255)/255,randint(0,255)/255)
            # bgcolor(randint(0,255)/255,randint(0,255)/255,randint(0,255)/255)
#Billard()


