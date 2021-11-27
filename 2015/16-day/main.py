import re
import pandas as pd

with open('input.txt', 'r') as f:
    lines = f.readlines()

pattern1 = "Sue (\d+): (.*)"
pattern2 = "(\w+: \d+)"
sues = {}
for line in lines:
    sue_n, items_str = re.findall(pattern1, line)[0]
    items = {}
    for item in items_str.split(','):
        item_name, n = item.split(':')
        items[item_name.strip()] = int(n)
    sues[int(sue_n)] = items        

df = pd.DataFrame(sues).T

eq_or_na = lambda c, n: df[c].isna() | (df[c] == n)
ge_or_na = lambda c, n: df[c].isna() | (df[c] > n)
le_or_na = lambda c, n: df[c].isna() | (df[c] < n)

df_out = df[
    eq_or_na('children', 3) &
    eq_or_na('cats', 7) &
    eq_or_na('samoyeds', 2) &
    eq_or_na('pomeranians', 3) &
    eq_or_na('akitas', 0) &
    eq_or_na('vizslas', 0) &
    eq_or_na('goldfish', 5) &
    eq_or_na('trees', 3) &
    eq_or_na('cars', 2) &
    eq_or_na('perfumes', 1)
]

aunt1 = df_out.index[0]

df_out = df[
    eq_or_na('children', 3) &
    ge_or_na('cats', 7) &
    eq_or_na('samoyeds', 2) &
    le_or_na('pomeranians', 3) &
    eq_or_na('akitas', 0) &
    eq_or_na('vizslas', 0) &
    le_or_na('goldfish', 5) &
    ge_or_na('trees', 3) &
    eq_or_na('cars', 2) &
    eq_or_na('perfumes', 1)
]

aunt2 = df_out.index[0]

print(f'A ::: Sue {aunt1}')
print(f'B ::: Sue {aunt2}')
