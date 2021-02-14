import numpy as np
import matplotlib.pyplot as plt

# membuat lingkaran
PI = np.pi
sudut = np.linspace(0,2*PI,100)
radius = 5

x = radius * np.cos(sudut)
y = radius * np.sin(sudut)

plt.figure(1)
plt.plot(x,y)
# cek matplotlib
x1 = [1,2,3,4,5]
y2 = [1,2,3,4,5]

# inisialisasi plot
plt.figure(2)
plt.plot(x1,y2)

# memanpilkan
plt.show()