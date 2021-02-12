import numpy as np

a = np.array((
              [1,2,3],
              [4,5,6]
            ))

print('matrix a dengan ukuran:',a.shape)
print(a)

#1. transpose matrix
print('\ntranspose matrix dari a')
print('cara pertama')
print(a.transpose())
# print('cara kedua')
# print(np.transpose(a))
# print('cara ketiga dengan menggunakan setter dan getter')
# print(a.T)
print('matrix a dengan ukuran:',a.shape)

# tidak akan berubah walau sudah di transpose
# print('matrix a dengan ukuran:',a.shape)
# print(a)


#2. flatten array, vector baris
print('\nflatten matrix a:')
print(a.ravel())
# print(np.ravel(a))
print('matrix a dengan ukuran:',a.shape)

#3. reshape matrix
print('\nreshape matrix a')
print(a.reshape(3,2))
# print("\n")
# print(a.reshape(6,1))
print('matrix a dengan ukuran:',a.shape)

#4. rezise matrix
print("\nrezise matrix a:")
a.resize(3,2)
print(a)
print('matrix a dengan ukuran:',a.shape)


