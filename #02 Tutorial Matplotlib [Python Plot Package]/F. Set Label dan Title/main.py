import numpy as np
import matplotlib.pyplot as plt

# Membuat Data
def sinusGenerator(amplitudo, frekuensi, waktu, theta):
    t = np.arange(0, waktu, 0.1)
    y = amplitudo * np.sin(2*frekuensi*t + np.deg2rad(theta))
    return t,y

amplitudo = 1
frekuensi = 1
theta = 0
waktu = 4

t,y = sinusGenerator(amplitudo,frekuensi,waktu,theta)

# Membuat Plot
plt.plot(t,y)

# Setting Title dan Label

# Title
judul = 'Grafik Sinusoidal\n'
rumus = r'$ \mathcal{Y} = A.sin(2 \omega t + \theta) $' + '\n'
parameter1 = r'$ A =  $' + str(amplitudo) + ' cm, '
parameter2 = r'$ \omega =  $' + str(frekuensi) + r'$ \mathit{Hz}$' +', '
parameter3 = r'$ \theta =  $' + str(theta) + r'$ ^{o} $'


plt.title(judul + rumus + parameter1 + parameter2 + parameter3)

# Label
plt.xlabel('waktu(detik)')
plt.ylabel('magnituda(cm)')


# Menampilka Plot
plt.show()