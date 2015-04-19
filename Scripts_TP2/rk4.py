# TP2 MNI cm3 2014-15

# Probleme : Solution d'une equation differentielle ordinaire
# Methode : Runge-Kutta 4eme ordre 
# Test : y'=-cr*y, y(0)=1, x=(0,3)
# Solution analytique: y=exp(-cr*x)

from math import *
import numpy as np
import matplotlib.pyplot as plt


#function
def f(x1,x2):
 return -x2*cr

print("===================================================")
print("Solution d''une equation differentielle ordinaire")
print(" Test : y'=-cr*y, y(0)=1, x=[0,2]")
print("===================================================")


#pas integration
h=input("pas d'integration h=? ")

cr=8;

# condition initiale
y0=1.
x0=0.
# intervalle integration
a=0. 
b=2.
# nombre pas integration
Np=int((b-a)/h)+1

# Methode RK4: solution numerique 
x=np.zeros(Np)
y=np.zeros(Np)
x[0]=x0
y[0]=y0
xp=x0 
yp=y0
for i in range(1,Np):
# x(i), y(i) - point courant, xp, yp - point precedent
  x[i]=xp+h
  k1=f(xp,yp)
  k2=f(xp+0.5*h,yp+0.5*h*k1)
  k3=f(xp+0.5*h,yp+0.5*h*k2)
  k4=f(xp+h,yp+h*k3)
  y[i]=yp+h*(k1+2.*k2+2.*k3+k4)/6.
  xp=x[i]
  yp=y[i]

#Solution analytique :
xa=x
ya=np.exp(-xa*cr)
plt.plot(xa,ya,'-r',label='theorique')
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x,y,'ob',label='RK4')
plt.legend(loc='upper right')
plt.show()

