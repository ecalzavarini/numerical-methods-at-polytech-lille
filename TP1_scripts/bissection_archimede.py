# TP1 MNI cm3 2014-15
#
# Probleme : Boule solide dans l'eau (principe Archimede)
# Racine eq. nonlineaire

from math import *
import numpy as np
import matplotlib.pyplot as plt


# fonction
def f(x):
   return x**3-3.*R*x**2+4.*rho1/rhoF*R**3

# rayon de la boule
R=0.125
# masse volumique du fluide (eau)
rhoF=1000.

print("")
print("========================================================")
print("Boule solide dans un fluide (eau) - principe Archimede")
print("Calcul de la hauteur ha laquelle la boule s'enfonce")
print("Rayon de la boule: R = %6.4f" %R)
print("Masse volumique eau: rhoF = %6.4f" %rhoF)
print("========================================================")
print("")
rho1=input("Masse volumique de la boule=?")

# graphique
xgM=4.*R
N=20
dxg=xgM/(1.*N)
xg=np.linspace(0,4*R,N)
yg=f(xg)
ygg=np.zeros(N)
plt.plot(xg,yg,'r',label="f(x)")
plt.plot(xg,ygg,'b')
plt.axis([0, xgM, -0.05, 0.05])
plt.xlabel("x")
plt.legend(loc='lower right')
plt.show()

if (rho1>rhoF):
   print("\nLa boule coule: rho1 = %6.4f, rhoF = %6.4f \n" %(rho1,rhoF))
elif (rho1==rhoF):
  print("\nhauteur h = 2R = %6.4f, rho1 = rhoF = %6.4f \n" %(2.*R,rhoF))
else:
# solution par methode bissection
   print("\nRacine eq nonlineaire : methode de bissection (dichotomie)")
   print("Bornes intervalle recherche: 0<h<2R")
   bi=input("Borne inf de l'intervalle de recherche bi=?")
   bs=input("Borne sup de l'intervalle de recherche bs=?")
   eps=input("Precision eps=?")
   maxcpt=input("Max nombre iterations maxcpt=?")

   if (f(bi)*f(bs)>0):
     print("\nPROBLEME DE SEPARATION DE RACINE \n")
   else:
     cpt=0
     d=abs(bs-bi)
     x=(bi+bs)/2.
     while d>eps:
        cpt=cpt+1
# arret de la methode si le nombre d'iterations devient trop grand
        if (cpt>maxcpt):
          print("\nnombre iterations > maxcpt \n")
          break
        if f(x)*f(bi)> 0:
          bi=x
        else:
          bs=x
        d=bs-bi
        x=(bi+bs)/2.
     if (cpt<maxcpt): 
       print("\nSOLUTION:")
       print("hauteur h = %2.8f" %x)
       print("precision = %1.8f" %d)
       print ("f(h) = %1.8f" %f(x))
       print("Nombre d''iterations = %d \n" %cpt)


