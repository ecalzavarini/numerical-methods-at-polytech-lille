# TP1 MNI cm3 2014-15
#
# Racine eq. nonlineaire
# Methode : Newton (tangente) 

from math import *
import numpy as np
import matplotlib.pyplot as plt


# fonction
def f(x):
   return x**4-2.*x**3-11.*x**2+12.*x
# derivee
def df(x):
   return 4.*x**3-6.*x**2-22.*x+12.


print("")
print("========================================================")
print("Racine d'une equation nonlineaire")
print("Methode de Newton (tangente)")
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

   x0=8.2
   eps=10.**(-k)
   bi=3.2
   bs=8.2
   a=bi
   b=bs

   if (f(bi)*f(bs)>0):
     print("\nPROBLEME DE SEPARATION DE RACINE \n")
   else:
     cpt=1
     x1=x0-f(x0)/df(x0)
     d=abs(x0-x1)
     while d>eps:
        cpt=cpt+1
# arret de la methode si le nombre d'iterations devient trop grand
        if (cpt>maxcpt):
          print("\nnombre iterations > maxcpt \n")
          break
        x0=x1
        x1=x0-f(x0)/df(x0)
        d=abs(x0-x1)
     if (cpt<maxcpt): 
       print("\nSOLUTION:")
       print("eps = %2.8f" %eps)
       print("racine x1 = %2.8f" %x1)
       print("precision = %1.8f" %d)
       print ("f(x1) = %1.8f" %f(x1))
       print("x1 - xs = %1.8f" %(x1-xs))
       print("Nombre d''iterations = %d \n" %cpt)


