import numpy as np

with open('input.txt', 'r') as f:
    raw = f.readlines()

class Grid:
    def __init__(self, raw):
        raw_list = [list(line.strip()) for line in raw]
        self.grid = np.array(raw_list)
        self.ncol, self.nrow = self.grid.shape

        self.grid[0, 0] = '#'
        self.grid[0, self.ncol - 1] = '#'
        self.grid[self.nrow - 1, 0] = '#'
        self.grid[self.nrow - 1, self.ncol - 1] = '#'

    def get_neighbors(self, r, c):
        nb_ix = [
            (r - 1, c - 1), (r - 1,     c), (r - 1, c + 1),
            (r    , c - 1),                 (r    , c + 1),
            (r + 1, c - 1), (r + 1,     c), (r + 1, c + 1)
        ]

        nb_ix_trim = [
            (r, c) for r, c in nb_ix
            if 0 <= r <= self.nrow - 1 and 0 <= c <= self.ncol - 1
        ]

        return np.array([self.grid[r, c] for r, c in nb_ix_trim])


    def new_state(self, r, c):
        if (r, c) in [(0, 0), (0, self.ncol - 1), (self.nrow - 1, 0), (self.nrow - 1, self.ncol - 1)]:
            return '#'

        nbs = self.get_neighbors(r, c)
        this_light = self.grid[r, c]
        nbs_on = np.sum(nbs == '#')

        if this_light == '#':
            return '#' if 2 <= nbs_on <= 3 else '.'

        if this_light == '.':
            return '#' if nbs_on == 3 else '.'

    def iterate(self):
        new_grid = self.grid.copy()

        for r in range(self.nrow):
            for c in range(self.ncol):
                new_grid[r, c] = self.new_state(r, c)

        self.grid = new_grid

g = Grid(raw)

for _ in range(100):
    g.iterate()

n_on = (g.grid == '#').sum()
print(f"B ::: Number of lights on: {n_on}")
