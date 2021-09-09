from functools import reduce
from itertools import product
import numpy as np
import networkx as nx

input_ = 'hxtvlmkl'

# PART 1 ======================================================================

def khash_1(lengths, arr, pointer=0, skip=0):
    n = len(arr)

    for l in lengths:
        ix = np.arange(pointer, pointer + l) % n
        arr[ix] = arr[ix][::-1]
        pointer += (l + skip) % n
        skip += 1

    return arr, pointer, skip

def khash_64(seq, n=256):
    lengths = [ord(c) for c in seq]
    lengths.extend([17, 31, 73, 47, 23])
    arr = np.arange(256)

    pointer = 0
    skip = 0
    for _ in range(64):
        arr, pointer, skip = khash_1(lengths, arr, pointer, skip)

    sparse_hash = ''
    ix = np.arange(256) // 16
    xor = lambda a, b: a ^ b
    to_hex_str = lambda n: hex(n)[2:].zfill(2)

    for i in range(16):
        hash_num = reduce(xor, arr[ix == i])
        hash_hex = to_hex_str(hash_num)
        sparse_hash += hash_hex

    return sparse_hash

def str_to_bin(s):
    knot_hash = khash_64(s)
    return bin(int(knot_hash, 16))[2:].zfill(128)

lines = [str_to_bin(f"{input_}-{i}") for i in range(128)]
regions = sum(int(c) for c in ''.join(lines))
print(f"There are {regions} regions occupied in the grid.")

# PART 2 ======================================================================

mx = np.array([[int(i) for i in line] for line in lines ])

G = nx.Graph()

ix_to_lbl = lambda r, c: f'{r}::{c}'

for r, c in product(range(128), range(128)):
    # If not occupied, skip
    if mx[r, c] == 0:
        continue

    # Add self
    G.add_edge(ix_to_lbl(r, c), ix_to_lbl(r, c))

    # N neighbor
    if r != 0 and mx[r - 1, c] == 1:
        G.add_edge(ix_to_lbl(r, c), ix_to_lbl(r - 1, c))

    # S neighbor
    if r != 127 and mx[r + 1, c] == 1:
        G.add_edge(ix_to_lbl(r, c), ix_to_lbl(r + 1, c))

    # E neighbor
    if c != 127 and mx[r, c + 1] == 1:
        G.add_edge(ix_to_lbl(r, c), ix_to_lbl(r , c + 1))

    # W neighbor
    if c != 0 and mx[r, c - 1] == 1:
        G.add_edge(ix_to_lbl(r, c), ix_to_lbl(r , c - 1))

nodes = set(G.nodes)
n_groups = 0
while nodes:
    node = min(nodes)
    group = nx.descendants(G, node)
    group.add(node)
    n_groups += 1
    nodes -= group

print(f"There are {n_groups} groups in this grid.")
