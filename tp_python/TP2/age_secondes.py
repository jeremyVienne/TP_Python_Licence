#!/usr/bin/env python3
from datetime import *

def nbre_sec_depuis_1900(annee,mois,jour):
      

      nbre_sec_jour=60*60*24
      nbre_sec_an=nbre_sec_jour*365.2425
      nbre_sec_mois=nbre_sec_an/12
      aujourdhui = date.today()
      aujourdhui_an = aujourdhui.year
      aujourdhui_mois=aujourdhui.month
      aujourdhui_jour= aujourdhui.day

      ecart_an=aujourdhui_an-annee
      ecart_jour=aujourdhui_jour-jour
      ecart_mois=aujourdhui_mois-mois


      if (ecart_mois<0):
        ecart_an=ecart_an-1
        ecart_mois=12-ecart_mois
      resultat = ecart_an*nbre_sec_an + ecart_jour*nbre_sec_jour + ecart_mois*nbre_sec_mois
      return resultat
      
      
      #print("l'ecart entre la date de référence et aujourd'hui vaut en seconde: ",resultat)
      #print("Vous avez: ", resultat, " en secondes ")

ref_an_naissance = int(input("An? "))
ref_mois_naissance=int(input("mois? "))
ref_jour_naissance=int(input("jour? "))


print( " Vous avez en secondes: ",nbre_sec_depuis_1900(ref_an_naissance,ref_mois_naissance, ref_jour_naissance))




