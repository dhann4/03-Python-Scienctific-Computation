import numpy as np

#perkalian dot
a1 = np.array([1,3])
b1 = np.array([3,0])

c1 = np.dot(a1,b1)

#perkalian cross
a2 = np.array([1,2,0])
b2 = np.array([2,1,0])

c2 = np.cross(a2,b2) # minus
c3 = np.cross(b2,a2) # plus

print(c3)