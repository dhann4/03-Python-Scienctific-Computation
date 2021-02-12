import numpy as np

# list python
a = [1,2,3,4,5]
b = [6,7,8,9,10]

# penjumlahan dengan list python
list_py = a + b

# pengurangan
# list_py = a - b
# hasil nya akan error karena list tidak bisa di kurangi dengan list
# berkalu pada perkalian dan pembagian




# array numpy
anp = np.array([1,2,3,4,5])
bnp = np.array([6,7,8,9,10])

'''
tidak menjumlahkan angka di dalam list a dan angka di dalam list b perkomponen
yang terjadi hanyalah list b di tempelkan ke dalam list a dan hasil nya adalah
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''

# ELEMENTWISE operation (jadi operasi nya per elemen kalau di numpy array)
# penjumlahan dengan array numpy
array_numpy = anp + bnp
'''
yang terjadi adalah, komponen di dalam anp di tambahkan dengan komponen di dalam bnp
setiap perkomponen nya dan hasil nya adalah
[ 7  9 11 13 15]
'''
# pengurangan
array_numpy = anp - bnp
'''
jangan kaget, jika tampilan nya adalah
[-5 -5 -5 -5 -5]

karena:
1-6 = -5
2-7 = -5
3-8 = -5
4-9 = -5
5-10 = -5
'''
# perkalian
array_numpy = anp * bnp
'''
hasil nya adalah : [ 6 14 24 36 50]
'''
# pembagian
array_numpy = anp / bnp
'''
hasil nya adalah : [0.16666667 0.28571429 0.375      0.44444444 0.5       ]
'''
# kuadrat
array_numpy = anp**2 # atau bnp**2
'''
hasil nya : [ 1  4  9 16 25]
'''


# multidimensi array numpy
c = np.array(([1,2,3],[4,5,6]))
d = np.array(([7,8,9],[-1,-2,-3]))

array_numpy = c + d
array_numpy = c - d
array_numpy = c * d
array_numpy = c / d
print(array_numpy)