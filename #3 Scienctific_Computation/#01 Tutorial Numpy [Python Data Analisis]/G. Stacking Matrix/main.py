# stacking matrix atau menumpuk matrixseperti list di python

import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

# caranya adalah
c = np.hstack((a,b)) # h = horizontal / kesamping
d = np.vstack((a,b)) # v = vertical / dari atas ke bawah dan sebaliknya

# untuk matrix
aM = np.zeros((2,3))
bM = np.ones((2,3))

cM = np.hstack((aM, bM))
dM = np.vstack((aM, bM))
'''
untuk penggunaan vstack di dM harus hati - hati karena

jika di
aM = np.zeros((2,2))
cM = np.hstack((aM, bM))
print(cM)

hasil nya adalah
[[0. 0. 1. 1. 1.]
 [0. 0. 1. 1. 1.]]
 

sedangkan kalau
bM = np.ones((2,3))
dM = np.vstack((aM, bM))
print(dM)

hasilnya akan error karena berbeda ukuran dengan si aM
'''

print(dM)