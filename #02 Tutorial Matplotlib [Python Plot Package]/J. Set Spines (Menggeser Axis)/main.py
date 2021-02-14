import numpy as np
import matplotlib.pyplot as plt


# Membuat Data
sudut = np.arange(0,360,1)
y = np.sin(np.deg2rad(sudut))

# Membuat Plot
plt.plot(sudut,y)

# Title
plt.title("Grafik Sinusoidal")

# Label
plt.text(190 ,1 ,"magnituda")
plt.text(360, 0.1 ,"sudut")

# Set Ticks
plt.yticks([-1, -0.5, 0, 0.5, 1])
plt.xticks(
    [0         , 90         , 180         , 270         , 360         ],
    [r'${0}^o$', r'${90}^o$', r'${180}^o$', r'${270}^o$', r'${360}^o$']
)


# Mengakses Axis
ax = plt.gca()
# Menggeser Axis
ax.spines['left'].set_position(('data',180))
ax.spines['bottom'].set_position(('data',0))
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Menampilkan Plot
plt.show()