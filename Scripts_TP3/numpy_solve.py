import numpy as np 

#Matrix A
A = np.array([[6,2,2,1],[2,8,2,1],[4,2,16,8],[2,4,1,9]] ,float)
#vector b                                                                                                                     
b = np.array([1,2,4,1],float)

x = np.linalg.solve(A, b)
print(x)
