import numpy as np
import matplotlib.pyplot as plt

"""
    Step :
    1. Membuat Data
    2. Membuat Plot
    3. Menampilkan Plot
"""
#1. Membuat Data (sederhana)
x = np.array([1,2,3,4,5])
y = np.array([1,4,9,16,25])
y2 = np.array([1,16,81,256,625])

#2. Membuat Plot
plt.plot(x,y)
plt.plot(x,y2)

#3. Menampilkan Plot
plt.show()