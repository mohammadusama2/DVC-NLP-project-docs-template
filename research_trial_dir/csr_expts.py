import numpy as np
from scipy.sparse import csr_matrix

#Sparse matrix have lot of zeroes
A = np.array([
    [1,0,0,0,0,1,0],
    [0,1,0,0,0,0,0],
    [0,0,0,0,1,0,0]
])

print(A)

S = csr_matrix(A)

print(S)
print(type(S))


#gettin back original results
B = S.todense()
print(B)