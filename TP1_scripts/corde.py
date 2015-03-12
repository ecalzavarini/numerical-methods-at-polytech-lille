# TP1 MNI cm3 2012-13
# Stefano Berti

# Probleme : Racine d'une equation nonlineaire
# Methode : de la corde
# Test : f(x)=x^3+x^2-3x-3=0 dans [1,2]
# Solution : x*=1.73205

from math import *
import numpy as np
import matplotlib.pyplot as plt


# fonction
def f(x):
   return x**3+x**2-3.*x-3.

print("")
print("========================================================")
print("Racine eq nonlineaire : methode de la corde")
print("")
print("========================================================")
bi=input("Borne inf de l'intervalle de recherche bi=?")
bs=input("Borne sup de l'intervalle de recherche bs=?")
eps=input("Precision du resultat eps=?")
maxcpt=input("Max nombre iterations maxcpt=?")

# graphique
xgM=5.
N=100
dxg=xgM/(1.*N)
xg=np.linspace(0,xgM,N)
yg=f(xg)
ygg=np.zeros(N)
plt.plot(xg,yg,'r',label="f(x)")
plt.plot(xg,ygg,'b')
plt.axis([0, xgM, -50, 200])
plt.xlabel("x")
plt.legend(loc='upper left')
plt.show()

a=bi
b=bs

if (f(bi)*f(bs)>0):
  print("PROBLEME DE SEPARATION DE RACINE")
else:
  cpt=0
  x0=(a*f(b)-b*f(a))/(f(b)-f(a))
  d=abs(b-a)
  while d>eps:
    cpt=cpt+1
# arret de la methode si le nombre d'iterations devient trop grand
    if (cpt>maxcpt):
      print("nombre iterations > maxcpt")
      break
    if (f(x0)*f(b)<0):
      a=x0
    else:
      b=x0
    x1=(a*f(b)-b*f(a))/(f(b)-f(a))
    d=abs(x1-x0)
    x0=x1

if (cpt<maxcpt):
  print("\nSOLUTION:")
  print("eps = %2.8f" %eps)
  print("racine x* = %2.8f" %x1)
  print("precision = %1.8f" %d)
  print ("f(x*) = %1.12f" %f(x1))
  print("Nombre d'iterations = %d \n" %cpt)

