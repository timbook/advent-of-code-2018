from itertools import combinations
import re

with open('../data/02-input.txt', 'r') as f:
    data = f.read().splitlines()

rows = [row.strip().split('\t') for row in data]
rows = [[int(val) for val in row] for row in rows]

maxes = [max(row) for row in rows]
mins = [min(row) for row in rows]

checksum = sum(mx - mn for (mx, mn) in zip(maxes, mins))

print("::: PART A")
print(f"Checksum = {checksum}\n")

#==============================================================================

def get_div(xs):
    for a, b in combinations(xs, 2):
        if a % b == 0:
            return(a/b)
        elif b % a == 0:
            return(b/a)

divs = [get_div(row) for row in rows]
checksum_b = int(sum(divs))

print("::: PART B")
print(f"Checksum = {checksum_b}")
