import numpy as np

a = np.array(([1,2],
              [3,4]))
b = np.ones([2,2])

print("Matrix a:")
print(a)

print("Matrix b:")
print(b)

#perkalian biasa
c = a*b
print("perkalian biasa:")
print(c)

# perkalian matrix ada dua cara
# yang pertama dengan menggunakan np.dot()
d1 = np.dot(a,b)
print("perkalian matrix pertama:")
print(d1)
'''
hasil nya adalah 3 7 3 7, maksud nya adalah

matrix a kita punya angka   [1 2]   1   +   2

                            [3 4]   3   +   4
                            
                                    x       x
                                    
matrix b kita punya angka   [1 1]   1   +   1

                            [1 1]   1   +   1


proses nya adalah=      [1.1+2.1    1.1+2.1]    1x1 = 1     2x1 = 2     1+2 = 3
                        [                  ]
                        [3.1+4.1    3.1+4.1]    3x1 = 3     4x1 = 4     3+4 = 7
                                                Kurang lebih begini

dan hasil nya adalah    [[3. 3.]
                         [7. 7.]]
                         
'''
# cara kedua dengan objek b di masukkan ke dalam fungsi dot yang nempel di a contoh nya
print("perkalian matrix kedua:")
d2 = a.dot(b)
print(d2)