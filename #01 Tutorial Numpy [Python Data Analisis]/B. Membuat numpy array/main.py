import numpy as np

#1. membuat vector
a1 = np.array([1, 2, 3, 4, 5])
a2 = np.array([1.5, 2.5 ,3.5, 4, 5]) # membuat float

#2. membuat vector dengan range
b = np.arange(1,10,1)
# c = np.zeros(5) menampilkan angka nol yang di kali 5 di dalam array numpy
# c = np.ones(5) menampilkan angka satu yang di kali 5 di dalam array numpy

'''
angka 1 pertama adalah batas bawah
angka 10 kedua adalah batas atas
angka 1 terakhir adalah step
'''
# untuk perbedaan
b1 = np.arange(1,10,2)
b2 = np.arange(1,10,0.5)


#3. membuat linspace
c = np.linspace(1,10,4)
'''
artinya adalah menampilkan 4 angka dari 1-10 dengan jarak yang sama
'''

#4. array multidimensi / matrix
d = np.array([ (1,2,3) , (4,5,6)])
'''
(1,2,3) adalah baris pertama
(4,5,6) adalah baris kedua
'''

#4a. matrix dengan nilai nol
d1 = np.zeros((5,5))
'''
menampilkan matrix dengan nilai 0 yang di kali 5
'''
d2 = np.ones((5,5))

#4b.  matrix identitas
#a. cara pertama
d3 = np.identity(5)
'''
menampilkan matrix yang isi nya adalah nol dan terdapat angka 1 di dalam matrix nya dengan bentuk diagonal
'''
#b. cara kedua
d4 = np.eye(5)


# display
print(d4)