import numpy as np

# multitype
dtipe = [('nama','S10'),('tinggi',int)]
data = [
    ('Ucup', 130),
    ('Otong', 100),
    ('Mario', 190)
]

a = np.array(data, dtype= dtipe)
print(a)

print(np.sort(a, order='tinggi'))
print(np.sort(a, order='nama'))