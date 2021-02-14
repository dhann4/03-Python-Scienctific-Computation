import numpy as np
import matplotlib.pyplot as plt

# Membuat Data
def sinusGenerator(amplitudo, frekuensi, waktu, theta):
    t = np.arange(0, waktu, 0.1)
    y = amplitudo * np.sin(2*frekuensi*t + np.deg2rad(theta))
    return t,y

t,y = sinusGenerator(1,1,4,0)

# Membuat Plot
plt.plot(t,y)

# Setting Axis, minimum dan maximum
plt.axis([0,4,-1,1])


# Menampilka Plot
plt.show()