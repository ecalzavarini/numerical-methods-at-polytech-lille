# TP2 MNI cm3 2014-15
#
# Probleme : Solution d'une equation differentielle ordinaire
# Methode : Euler et point au milieu
# Test : y'=cos(x), y(0)=0, x=[0, 2*pi]
# Solution analytique: y=sin(x)

from math import *
import numpy as np
import matplotlib.pyplot as plt


#function
def f(x):
 return cos(x)

print("===================================================")
print("Solution d''une equation differentielle ordinaire")
print(" Test : y'=cos(x), y(0)=0, x=[0,2*pi]")
print("===================================================")
#pas integration
h=input("pas d'integration h=? ")
# condition initiale
y0=0.
x0=0.
# intervalle integration
a=0. 
b=2.*pi
# nombre pas integration
Np=int((b-a)/h)+1

# Methode d'Euler-Cauchy
x=np.zeros(Np)
y=np.zeros(Np)
x[0]=x0
y[0]=y0
xp=x0 
yp=y0
for i in range(1,Np):
# x(i), y(i) - point courant, xp, yp - point precedent
  x[i]=xp+h
  y[i]=yp+h*f(xp)
  xp=x[i]
  yp=y[i]
#Solution numerique Euler-Cauchy
x1=x
y1=y

# Methode du point au milieu
x=np.zeros(Np)
y=np.zeros(Np)
x[0]=x0
y[0]=y0
xp=x0 
yp=y0
for i in range(1,Np):
## x(i), y(i) - point courant, xp, yp - point precedent
  x[i]=xp+h
  y[i]=yp+h*f(xp+h/2.)
  xp=x[i]
  yp=y[i]
#Solution numerique Point au milieu 
x2=x
y2=y

#Solution analytique :
xa=x
ya=np.sin(xa)
plt.plot(xa,ya,'r',label='theorique')
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x1,y1,'b',label='euler')
plt.plot(x2,y2,'g',label='point au milieu')
plt.legend(loc='upper right')
plt.show()


# Comparaison en x=3*%pi/2
xs=3.*pi/2.
k=int(xs/h+1)
print("===============================")
print("Comparaison en xs=3pi/2")
print("Pas integration h = %f" %h)
print("Theorique: xs = %f; ys = %f" %(xs,sin(xs)))
#print("Euler Cauchy: x1 = %f; y1 = %f" %(x1[k],y1[k]))
print("Tangente Amelioree: x2 = %f; y2 = %f" %(x2[k],y2[k]))
print("===============================")
