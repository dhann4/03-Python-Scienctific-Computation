import numpy as np

a = np.array([(1,-1),
              (1,1)])
print('Matrix a')
print(a,'\n')

#1. Inverse matrix
a_inv = np.linalg.inv(a)
print('Inverse matrix a')
print(a_inv, "\n")

# perkalian dot
print('Perkalian dot untuk Inverse matrix')
print(np.dot(a,a_inv),'\n')


#2. Determinan matrix
det_a = np.linalg.det(a)
det_a_inv = np.linalg.det(a_inv)
print('Determinan matrix a')
print(det_a,'\n')
print('Determinan Inverse matrix a')
print(det_a_inv)