#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import gauss_pivot_partiel


print("PROBLEM 1")
#Dimension of matrix 
N = 4
# Extended matrix N,N+1
A = np.array([[6,2,2,4,1],[2,8,2,1,2],[4,2,16,8,4],[2,4,1,9,1]] ,float) 
# Now we solve the system
x = [0 for i in range(N)]
x=gauss_pivot_partiel.Gauss(A,N)
print("Solution x = "+str(x))


print("PROBLEM 2")
#Dimension of matrix 
N = 3
# Extended matrix N,N+1
A = np.array([[19,5,7,8],[2,7,2,2],[1,6,11,1]] ,float) 
# Now we solve the system
x = [0 for i in range(N)]
x=gauss_pivot_partiel.Gauss(A,N)
print("Solution x = "+str(x))

print("PROBLEM 3")
#Dimension of matrix 
N = 3
# Extended matrix N,N+1
A = np.array([[4,-1,7,7],[9,0,5,8],[-2,6,1,6]],float) 
# Now we solve the system
x = [0 for i in range(N)]
x=gauss_pivot_partiel.Gauss(A,N)
print("Solution x = "+str(x))


print("PROBLEM 4")
#Dimension of matrix 
N = 4
# Extended matrix N,N+1
A = np.array([[7,0,1,-1,4],[3,10,5,0,3],[0,4,9,2,-3],[1,-5,3,15,12]] ,float)
# Now we solve the system
x = [0 for i in range(N)]
x=gauss_pivot_partiel.Gauss(A,N)
print("Solution x = "+str(x))

