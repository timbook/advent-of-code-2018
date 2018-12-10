import re
import numpy as np

with open('../data/10-input.txt', 'r') as f:
    data = f.read().splitlines()

rx = r"position=<(.*), (.*)> velocity=<(.*), (.*)>"

def process_line(line):
    x, y, vx, vy = re.findall(rx, line)[0]
    return int(x), int(y), int(vx), int(vy)

data = [process_line(line) for line in data]

class Grid:
    def __init__(self, data):
        self.data = data
        self.xmax = max(val[0] for val in data)
        self.xmin = min(val[0] for val in data)
        self.ymax = max(val[1] for val in data)
        self.ymin = min(val[1] for val in data)
        self.width = self.xmax - self.xmin
        self.height = self.ymax - self.ymin

    def make_grid(self):
        self.grid = np.zeros((self.width, self.height)).astype('str')
        self.reset_grid(' ')

    def populate_grid(self):
        for x, y, xv, yv in self.data:
            self.grid[x - self.xmin - 1, y - self.ymin - 1] = '#'

    def inc_grid(self):
        data = [(x + vx, y + vy, vx, vy) for x, y, vx, vy in self.data]
        self.__init__(data)

    def reset_grid(self, char):
        self.grid[:, :] = char

    def display_grid(self):
        for i in range(self.grid.shape[0]):
            row = self.grid[i, :]
            print(''.join(row))

grid = Grid(data)

for i in range(10144):
    grid.inc_grid()

grid.make_grid()
grid.populate_grid()
grid.display_grid()
