import numpy as np

# one dimension
a = np.floor(np.random.rand(1,6)*10)
print(a)

print('\nnilai max dari a: ',a.max())
print('posisi max dari a:',a.argmax())

print('\nnilai min dari a: ',a.min())
print('posisi min dari a: ',a.argmin())

print('\nmengurutkan nilai a:')
print(np.sort(a))

print('\nmengurutkan posisi nilai a:')
print(np.argsort(a))