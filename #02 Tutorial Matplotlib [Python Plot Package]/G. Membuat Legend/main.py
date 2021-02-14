import numpy as np
import matplotlib.pyplot as plt

# Membuat Data
def sinusGenerator(amplitudo, frekuensi, waktu, theta):
    t = np.arange(0, waktu, 0.1)
    y = amplitudo * np.sin(2*frekuensi*t + np.deg2rad(theta))
    return t,y


t,y = sinusGenerator(1,1,4,0)
t1,y1 = sinusGenerator(1,1,4,90)

# Membuat Plot

# Contoh 1
# plt.plot(t,y, label="sin(0)")
# plt.plot(t1,y1, label="sin(90)")
#
# # Membuat Legend
# plt.legend()


# Contoh 2
# plt.plot(t,y, label="sin(0)")
# plt.plot(t1,y1, label="sin(90)")
#
# plt.legend(loc="upper center")

# Contoh 3
# plt.plot(t,y, label="sin(0)")
# plt.plot(t1,y1, label="sin(90)")
#
# plt.legend(loc="upper center", bbox_to_anchor = (0.5,-0.05))

# Contoh 4
plt.figure(1)
ax = plt.subplot(111)

plt.plot(t,y, label="sin(0)")
plt.plot(t1,y1, label="sin(90)")

box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width*0.7, box.height])

plt.legend(loc="upper center", bbox_to_anchor = (1.2,1))



# Menampilkan Plot
plt.show()