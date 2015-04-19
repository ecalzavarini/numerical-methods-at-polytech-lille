#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

# Methode : Jacobi (iterative)
# Version : verification si A est a diag dominante
# ****************************************************************

print("Solution d''un systeme lineaire Ax=b : methode de Jacobi")


def Jacobi(A,b,N):
  # check: diagonale dominante
  problem = 0
  for i in range(0,N) :
    # line i of the matrix
    linesum = np.sum(np.abs(A[[i]])) 
    element = np.abs(A[i][i])
    if element <= linesum - element :
      problem = 1             
 
  if problem == 0 :
    print("The matrix is diagonal dominant")
  else :
    print("The matrix is not diagonal dominant, aborting program.")
    exit()
      
# vecteur initial
  x0 = np.zeros(N)
  for i in range(0,N):
    x0[i] = input("vecteur initial, element no " + str(i) +" of "+str(N)+" : ")
# precision
  eps = input("precision epsilon ? " )



# xp- vect precedant. xn - vect nouveau
  xp=np.copy(x0)
# extraction de la diagonale (vecteur)
  d=np.diag(A)
# Matrice diagonale inverse
  invD= np.identity(N)/d
# elimination de la diagonale de A
  M=np.identity(N)*d-A

# Matrice Jacobi
  M=np.dot(invD,M)
# Vecteur Jacobi
  c=np.dot(invD,b)
# pour entrer dans la boucle
  prec=2*eps;

  it = 0
  while prec > eps:
    it=it+1
    xn=np.dot(M,xp)+c
    #print(xn)
  # compute the norm
    prec = 0
    for i in range(0,N):
      prec = prec + (xn[i]-xp[i])**2.0
    prec = np.sqrt(prec)
    xp=xn

#  print("Solution :")
#  print(xn)
  print("Nombre d''iterations it = " + str(it))
  return(xn)



