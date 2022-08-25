import numpy as np
from collections import Counter

lines = open('input.txt', 'r').readlines()

mx = np.array([list(line.strip()) for line in lines])

n, p = mx.shape

chars = []
for col in range(p):
    v = mx[:, col]
    c = Counter(v)
    chars.append(c.most_common()[0][0])

print(''.join(chars))

chars = []
for col in range(p):
    v = mx[:, col]
    c = Counter(v)
    chars.append(c.most_common()[-1][0])

print(''.join(chars))
