import numpy as np
from itertools import product
import pdb

with open("../data/18-input.txt") as f:
    lines = f.readlines()

# raw = """
# .#.#...|#.
# .....#|##|
# .|..|...#.
# ..|#.....#
# #.#|||#|#|
# ...#.||...
# .|....|...
# ||...#|.#|
# |.||||..|.
# ...#.|..|.
# """.strip().split('\n')

lines_split = [list(line.strip()) for line in lines]
# lines_split = [list(line.strip()) for line in raw]

land = np.array(lines_split)
nrow, ncol = land.shape


def process_land(i, j, land):
    nb_locs = [
        (i - 1, j + 1), (i, j + 1), (i + 1, j + 1),
        (i - 1, j)    ,             (i + 1, j),
        (i - 1, j - 1), (i, j - 1), (i + 1, j - 1)
    ]

    # Find what neighbors look like
    nbs = []
    for i_nb, j_nb in nb_locs:
        if (0 <= i_nb <= land.shape[0] - 1) and (0 <= j_nb <= land.shape[1] - 1):
            nbs.append(land[i_nb, j_nb])

    if land[i, j] == '.':
        n_trees = sum(nb == '|' for nb in nbs)
        acre_out = '|' if n_trees >= 3 else '.'

    elif land[i, j] == '|':
        n_lumber = sum(nb == '#' for nb in nbs)
        acre_out = '#' if n_lumber >= 3 else '|'

    elif land[i, j] == '#':
        n_lumber = sum(nb == '#' for nb in nbs)
        n_trees = sum(nb == '|' for nb in nbs)
        acre_out = '#' if (n_lumber >= 1 and n_trees >= 1) else '.'

    return acre_out

def print_land(land):
    rows = [''.join(land[i,:]) for i in range(land.shape[0])]
    print('\n'.join(rows))

for t in range(10):
    new_land = np.empty((nrow, ncol), dtype=str)
    ijs = product(range(nrow), range(ncol))
    for i, j in ijs:
        new_land[i, j] = process_land(i, j, land)
    land = new_land

n_wood = np.sum(land == '|')
n_lumber = np.sum(land == '#')
print(n_wood * n_lumber)

print("::: PART A")
print(f"THE RESOURCE VALUE IS: {n_wood * n_lumber}")

# =============================================================================

land = np.array(lines_split)
for t in range(100000):
    new_land = np.empty((nrow, ncol), dtype=str)
    ijs = product(range(nrow), range(ncol))
    for i, j in ijs:
        new_land[i, j] = process_land(i, j, land)
    land = new_land

    if t % 1000 == 0:
        n_wood = np.sum(land == '|')
        n_lumber = np.sum(land == '#')
        print(f"{t} : {n_wood * n_lumber}")










