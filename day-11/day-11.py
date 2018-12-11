from grid import Grid
import numpy as np

serial_number = 5468

grid = Grid(serial_number)
grid.generate_power_levels()
grid.get_convolved_matrix(3)

max_row, max_col, max_val = grid.get_max_index()

print("::: PART A")
print(f"Max X,Y: ({max_row},{max_col})")
print(f"And it has a power level of {max_val}\n")

#==============================================================================

max_convolutions = [grid.convolve_and_max(s) for s in range(1, 300)]
max_level = max(map(lambda x: x[3], max_convolutions))
best_grid = list(filter(lambda x: x[3] == max_level, max_convolutions))[0]

print("::: PART B")
print(f"Max X,Y,S: {best_grid[:3]}")
print(f"And it has a power level of {best_grid[3]}")
