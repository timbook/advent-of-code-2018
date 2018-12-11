from itertools import product
import numpy as np

class Grid:
    def __init__(self, serial_number):
        self.N = 300
        self.mx = np.zeros((self.N, self.N), dtype=int)
        self.serial_number = serial_number

    def generate_power_levels(self):
        elements = product(range(1, self.N + 1), range(1, self.N + 1))
        for x, y in elements:
            self.add_power_level(x, y)

    def add_power_level(self, x, y):
        rack_id = x + 10
        power_level = rack_id * y
        power_level += self.serial_number
        power_level *= rack_id

        power_level_str = str(power_level)
        if len(power_level_str) >= 3:
            power_level = int(power_level_str[-3])
        else:
            power_level = 0

        power_level -= 5

        self.mx[x - 1, y - 1] = power_level

    def get_convolved_matrix(self, S):
        conv_mx = np.zeros((self.N - S, self.N - S), dtype=int)
        elements = product(range(1, self.N - S + 1), range(1, self.N - S + 1))
        for x, y in elements:
            conv_mx[x - 1, y - 1] = self.convolve(x, y, S)

        self.conv_mx = conv_mx

    def convolve(self, x, y, S):
        return np.sum(self.mx[(x - 1):(x + S - 1), (y - 1):(y + S - 1)])

    def get_max_index(self):
        max_row, max_col = np.where(self.conv_mx == self.conv_mx.max())

        max_row = max_row[0] + 1
        max_col = max_col[0] + 1

        return max_row, max_col, self.conv_mx.max()

    def convolve_and_max(self, S):
        self.get_convolved_matrix(S)
        max_row, max_col, max_val = self.get_max_index()
        return (max_row, max_col, S, max_val)

