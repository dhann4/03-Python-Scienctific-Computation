import numpy as np

#1. membuat matrix dengan tipe data tertentu
a = np.array(([1,2,3],[4,5,6]), dtype= float)
# a = np.array(([1,2,3],[4,5,6]), dtype= int)
# a = np.array(([1,2,3],[4,5,6]), dtype= bool)
# a = np.array(([1,2,3],[4,5,6]), dtype= str)


#2. membuat array dengan menggunakan function
def kuadrat(baris, kolom):
    return kolom ** 2

def jumlah(baris, kolom):
    return (baris + kolom)

b1 = np.fromfunction(kuadrat, (1, 10), dtype=int)

b2 = np.fromfunction(jumlah, (4,4), dtype= float)

#3. membuat array atau matrix dengan menggunakan iterable
iterable = (x*x for x in range(5))
# iterable = (x*2 for x in range(5))
c = np.fromiter(iterable, dtype= int)

#4. multitype array
dtipe = [('nama','S255'),('tinggi',int)]
data = [
    ("ucup", 150),
    ("otong", 160),
    ("mario", 180)
]

d = np.array(data, dtype= dtipe)
print(d)
print(d[0])



















