# TP1 MNI cm3 2014-15
#
# Racine eq. nonlineaire
# Methode : recherche dichotomique (bissection)

from math import *
import numpy as np
import matplotlib.pyplot as plt


# fonction
def f(x):
   return x**4-2.*x**3-11.*x**2+12.*x

print("")
print("========================================================")
print("Racine d'une equation nonlineaire")
print("Methode de bissection (dichotomie)")
print("Test : f(x)=x**4-2*x**3-11*x**2+12*x")
print("precision: eps=10^-k, k=1,...,6")
print("========================================================")
print("")

# max nombre iterations
maxcpt=1000
#solution exacte recherchee
xs=4

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

for k in range(1,6):

   eps=10.**(-k)
   bi=3.2
   bs=8.2
   a=bi
   b=bs

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
       print("eps = %2.8f" %eps)
       print("racine x = %2.8f" %x)
       print("precision = %1.8f" %d)
       print ("f(x) = %1.8f" %f(x))
       print("x - xs = %1.8f" %(x-xs))
       print("Nombre d''iterations = %d \n" %cpt)


