#!/usr/bin/env python3

#c=20
#f=(9/5)*c+32
#print("Une température de ",c, "°C correspond à une température de" ,f ,"F.")

#f=75
#c=(f-32)/(9/5)
#print("Une température de ",f, "F correspond à une température de" ,c ,"°C.")

def celsius_en_fahrenheit(c):
    f=(9/5)*c+32
    print("Une température de ", c,"°C correspond à une température de ", f, "F.")
c=25
celsius_en_fahrenheit(c)
help(celsius_en_fahrenheit)

def fahrenheit_en_celsius(f):
    c=(f-32)/(9/5)
    print("Une température de ",f, "F correspond à une température de" ,c ,"°C.")
f=77
fahrenheit_en_celsius(f)
help(fahrenheit_en_celsius)
    
