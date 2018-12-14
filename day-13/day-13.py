from items import Tracks

with open('../data/13-input.txt', 'r') as f:
    data = f.read().splitlines()

grid = Tracks(data)

while True:
    crash = grid.advance_carts()
    if crash:
        break

crash_row, crash_col = list(grid.crash_site)[0]

print("::: PART A")
print(f"It's at row {crash_row} and column {crash_col}\n")

#==============================================================================

grid = Tracks(data)

while True:
    done = grid.advance_and_drop()
    if done:
        break

survivor_row, survivor_col = (grid.carts[0].row, grid.carts[0].col)

print("::: PART B")
print(f"It's at row {survivor_row} and column {survivor_col}")
