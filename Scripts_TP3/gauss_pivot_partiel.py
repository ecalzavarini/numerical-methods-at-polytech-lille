#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

# function to print the extended matrix
def pprint(A):
    n = len(A)
    for i in range(0, n):
        line = ""
        for j in range(0, n+1):
            line += str(A[i][j]) + "\t"
            if j == n-1:
                line += "| "
        print(line)
    print("")


#function to solve linear system with gauss method
def Gauss(A,N):
    #Print the matrix
    print("\nExtended matrix (A|b)")
    pprint(A)

    # Gaussian elimination
    for k in range(0, N-1):

        # Partial pivoting
        idx = k
        #print("k "+str(k))
        for i in range(k+1, N):
            if abs(A[i][k]) > abs(A[k][k]) :
                idx = i
        # If the pivot is not the natural one
        if idx != k :
            #print("k "+str(k)+" ->  idx "+str(idx))
            #print("natural pivot was "+str(A[k][k])+" , but is better to choose "+str(A[idx][k]))
        # We swap the lines
            B = np.copy(A)
        # pprint(A)
            for i in range(0, N+1):
                A[k][i] = B[idx][i]
                A[idx][i] = B[k][i]    
        # pprint(A)

        # defining the pivot
        p = A[k][k]

        for i in range(k+1, N): 
            m = A[i][k]/p
            for j in range(k, N+1):
                A[i][j] = A[i][j] - m*A[k][j]

    print("After Gauss reduction")
    pprint(A)

        # Inverse substitution
    x = [0 for i in range(N)]

    for j in range(N-1, -1, -1):
        x[j] = A[j][N]
        for k in range(j+1,N):
            x[j] -= A[j][k] * x[k]
        x[j] /= A[j][j]
        
    #print("Solution x = "+str(x))
    return x


