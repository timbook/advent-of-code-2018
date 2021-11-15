import re
import numpy as np

class Grid:
    def __init__(self):
        self.grid = np.zeros((1000, 1000), dtype=int)

    def process_step(self, step):
        move, r1, c1, r2, c2 = re.findall('(.*) (\d+),(\d+) through (\d+),(\d+)', step)[0]
        r1, c1, r2, c2 = int(r1), int(c1), int(r2), int(c2)

        if move == 'turn on':
            self.grid[r1:(r2 + 1), c1:(c2 + 1)] = 1
        elif move == 'turn off':
            self.grid[r1:(r2 + 1), c1:(c2 + 1)] = 0
        elif move == 'toggle':
            self.grid[r1:(r2 + 1), c1:(c2 + 1)] = 1 - self.grid[r1:(r2 + 1), c1:(c2 + 1)]

    def process_step_b(self, step):
        move, r1, c1, r2, c2 = re.findall('(.*) (\d+),(\d+) through (\d+),(\d+)', step)[0]
        r1, c1, r2, c2 = int(r1), int(c1), int(r2), int(c2)

        if move == 'turn on':
            self.grid[r1:(r2 + 1), c1:(c2 + 1)] += 1
        elif move == 'turn off':
            self.grid[r1:(r2 + 1), c1:(c2 + 1)] -= 1
        elif move == 'toggle':
            self.grid[r1:(r2 + 1), c1:(c2 + 1)] += 2

        self.grid = np.maximum(self.grid, 0)


g = Grid()

with open('input.txt', 'r') as f:
    lines = f.readlines()

for line in lines:
    g.process_step(line.strip())

n_lit = np.sum(g.grid)
print("A :::")
print(f"There are {n_lit} lights lit")
print()

g = Grid()

for line in lines:
    g.process_step_b(line.strip())

brightness = np.sum(g.grid)
print("B :::")
print(f"The total brightness is {brightness}")
