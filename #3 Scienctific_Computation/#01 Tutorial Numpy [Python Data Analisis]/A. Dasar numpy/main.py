import numpy as np

a = np.array([1,2,3,4,5]) # di sebut array numpy
b = [1,2,3,4,5] # di sebut list python

print(a) # bedanya adalah list di numpy tidak ada koma nya
print(b) # sedangkan untuk list bawaan python ada koma nya
print("\n")

# beda lagi jika di tambah 1
a = a + 1 # menjumlah kan 1 pada tiap komponen
b = b + [1] # hanya menambah list di dalam list yang ada
print(a)
print(b)