# TP2 MNI cm3 2014-2015
# 
#
# Probleme : Trajectoire d'un objet lance
# et point d'impact
# Methode : Euler

# variables
# t - temps (discretise avec le pas h)
# y1 - abscisse x
# y2 - ordonnee z
# y3 - vitesse horizontale
# y4 - vitesse verticale

from math import *
import numpy as np

print("===================================================")
print("Calcul d'une trajectoire d'un objet de masse m")
print(" lance' a la vitesse v0 et a l'angle a0")
print(" coefficient de resistane de l'air k")
print(" position initiale x0=0, y0=0")
print("===================================================")
m=input("masse m=? " )
v0=input("vitesse initiale v0=? " )
a0=input("angle en degres a0=? " )
k=input("coefficient de resisitance de l'air k=? " )
h=input("pas d'integration h=? " )
Np=input("nombre de pas d'integration Np=? " )

# acceleration gravite
g=9.81
# conditions initiales
# position
x0=0
y0=0
y1=x0
y2=y0
# angle en radians
a0=a0*2.*pi/360.
# vitesse
y3=v0*cos(a0)
y4=v0*sin(a0)

# Methode d'Euler
t=0
print("")
print(" temps       x        z       vx       vz")
print("%f %f %f %f %f" %(t,y1,y2,y3,y4))
for i in range(1,Np):
 t=h*i
 y1n=y1+h*y3
 y2n=y2+h*y4
 y3n=y3+h*(-k*y3/m)
 y4n=y4+h*(-k*y4/m-g)
# ecriture: temps, position, vitesse
 print("%f %f %f %f %f" %(t,y1n,y2n,y3n,y4n))
 if y2n <0: 
  print("")
# ecriture point impact
  print("point d'impact:")
  print(" temps       x        z       vx       vz")
  print("%f %f %f %f %f" %(t,y1,y2,y3,y4))
  print("")
  break
 y1=y1n
 y2=y2n
 y3=y3n
 y4=y4n
