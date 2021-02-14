import numpy as np
import matplotlib.pyplot as plt


# Membuat Data
sudut = np.arange(0,360,1)
y = np.sin(np.deg2rad(sudut))

# Membuat Plot
plt.plot(sudut,y)
# Label
plt.ylabel("magnituda")
plt.xlabel(("sudut"))

# Set Ticks
plt.yticks([-1,0,1])
plt.xticks(
    [0         , 90         , 180         , 270         , 360         ],
    [r'${0}^o$', r'${90}^o$', r'${180}^o$', r'${270}^o$', r'${360}^o$']
)


# Menampilkan Plot
plt.show()