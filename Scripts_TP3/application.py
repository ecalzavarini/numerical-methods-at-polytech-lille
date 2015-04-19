import numpy as np
import matplotlib.pyplot as plt
# import Gauss function
import gauss_pivot_partiel 

n=7
x=np.array([-1.5,-1.0,-0.5,0.0,0.5,1.0,1.3],float)
y=np.array([0.9,1.2,-0.08,-2.0,-1.3,-0.5,0.5],float)

A00 = n
A01 = A10 = np.sum(x)
A02 = A11 = A20 = np.sum(x**2.)
A12 = A21 = np.sum(x**3.)
A22 = np.sum(x**4.)

b0 = np.sum(y) 
b1 = np.sum(x*y)
b2 = np.sum((x**2.)*y)

N=3
A=np.array([[A00,A01,A02,b0],[A10,A11,A12,b1],[A20,A21,A22,b2]],float)

#now we solve the system 
a = [0 for i in range(N)]
a = gauss_pivot_partiel.Gauss(A,N)
print("Solution a = "+str(a))

z=a[0]+a[1]*x+a[2]*x**2.


#Solution analytique :
plt.plot(x,y,'*',label='exp')
plt.plot(x,z,'r',label='a_0+a_1*x+a_2*x**2.')
plt.xlabel("x")
plt.ylabel("y")
plt.legend(loc='upper right')
plt.show()

