'''
Jika :
Y1  = 2.X1 + 3.X2
Y2  = X1   + 2.X2
Nilai untuk Y1 = 23 dan nilai untuk Y2 = 14,
Sedangkan untuk nilai X1 dan X2 masih belum di ketahui.

Carilah Nilai dari X1 dan X2
'''

import numpy as np

A = np.array([(2,3),
              (1,2)])
Y = np.array([23,14])

# menyelesaikan persamaan linear dengan Inverse
A_Inv = np.linalg.inv(A)

# Jawaban Soal :
X1 = np.dot(A_Inv,Y)
print(X1)
'''
untuk nilai X1 = 4 dan nilai X2 = 5

Y1 = 2.4 + 3.5 = 23
Y2 = 4 + 2.5 = 14
'''

# cara lain
X2 = np.linalg.solve(A,Y)
print(X2)



