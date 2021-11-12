from collections import deque

# Part A ======

step = 380
line = [0]
p = 1

for i in range(1, 2018):
    p = (p + step) % len(line)
    line.insert(p, i)
    p += 1

ix = line.index(2017)
print(line[ix + 1])

# Part B ======

step = 380
line = [0]
line_len = 1
second_num = None
p = 1

N_MAX = 50_000_000

for i in range(1, N_MAX + 1):
    p = (p + step) % line_len
    if p == 0:
        second_num = i
    p += 1
