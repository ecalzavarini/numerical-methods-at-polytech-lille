#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import jacobi



print("PROBLEM 1")
#Dimension of matrix 
N = 4
# Matrix A
A = np.array([[6,2,2,1],[2,8,2,1],[4,2,16,8],[2,4,1,9]] ,float)
#vector b
b = np.array([1,2,4,1],float)
# Now we solve the system
x = [0 for i in range(N)]
x=jacobi.Jacobi(A,b,N)
print("Solution x = "+str(x))


print("PROBLEM 2")
#Dimension of matrix 
N = 3
# Matrix A
A = np.array([[19,5,7],[2,7,2],[1,6,11]] ,float)
#vector b
b = np.array([8,2,1],float)
# Now we solve the system
x = [0 for i in range(N)]
x=jacobi.Jacobi(A,b,N)
print("Solution x = "+str(x))


print("PROBLEM 3")
#Dimension of matrix 
N = 3
# Matrix A
A = np.array([[4,-1,7],[9,0,5],[-2,6,1]] ,float)
#vector b
b = np.array([7,8,6],float)
# Now we solve the system
x = [0 for i in range(N)]
x=jacobi.Jacobi(A,b,N)
print("Solution x = "+str(x))


print("PROBLEM 4")
#Dimension of matrix 
N = 4
# Matrix A
A = np.array([[7,0,1,-1],[3,10,5,0],[0,4,9,2],[1,-5,3,15]] ,float)
#vector b
b = np.array([4,3,-3,12],float)
# Now we solve the system
x = [0 for i in range(N)]
x=jacobi.Jacobi(A,b,N)
print("Solution x = "+str(x))
