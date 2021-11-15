from itertools import groupby

def process(n):
    return ''.join([f"{len(list(g))}{k}" for k, g in groupby(str(n))])

n = '1113222113'
for _ in range(50):
    n = process(n)

print(len(n))
