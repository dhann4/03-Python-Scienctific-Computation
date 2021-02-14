import numpy as np
import matplotlib.pyplot as plt

"""
    Step nya:
    1. Membuat Data
    2. Membuat Plot
    3. Menampilkan Plot
"""
#1. Membuat Data (sinus generator) / (sin(2wt + theta))
# camel case jika huruf besar di awal kata berarti class
def sinusGenerator(amplitudo, frekuensi, waktu, theta):
    t = np.arange(0, waktu, 0.1)
    y = amplitudo * np.sin(2*frekuensi*t + np.deg2rad(theta))
    return t,y

#2. Membuat Plot
t1,y1 = sinusGenerator(1,1,4,0)
plt.plot(t1,y1)

# menambahkan warna
t2,y2 = sinusGenerator(1,1,4,30)
plt.plot(t2,y2, 'red')

t3,y3 = sinusGenerator(1,1,4,60)
plt.plot(t3,y3, 'green')

# membuat marker
t4,y4 = sinusGenerator(1,1,4,90)
plt.plot(t4,y4, 'y--')

t5,y5 = sinusGenerator(1,1,4,130)
plt.plot(t5,y5, 'c-X')


#3. Menampilkan Plot
plt.show()