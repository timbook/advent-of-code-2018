import pandas as pd

with open('input.txt', 'r') as f:
    lines = f.readlines()

def proc_line(line):
    return [int(n) for n in line.split()]

trips = [proc_line(line) for line in lines]

def is_tri(tup):
    a, b, c = tup
    cond1 = a + b > c
    cond2 = a + c > b
    cond3 = b + c > a
    return cond1 and cond2 and cond3

res_a = sum(is_tri(t) for t in trips)
print(f"A ::: Number of possible triangles = {res_a}")

df = pd.DataFrame(trips, columns = ['a', 'b', 'c'])
df['tri'] = df.index // 3

max_tri = df.tri.max()
res_b = 0
for i in range(max_tri + 1):
    t1 = df.loc[df.tri == i, 'a'].values
    t2 = df.loc[df.tri == i, 'b'].values
    t3 = df.loc[df.tri == i, 'c'].values
    res_b += int(is_tri(t1)) + int(is_tri(t2)) + int(is_tri(t3))

print(f"B ::: Number of possible triangles = {res_b}")
