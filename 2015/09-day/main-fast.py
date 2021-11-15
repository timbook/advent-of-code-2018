import re
from itertools import permutations

with open('input.txt', 'r') as f:
    lines = f.readlines()

class Route:
    def __init__(self, seq):
        self.seq = seq

    def __len__(self):
        return sum([hops[(a, b)] for a, b in zip(self.seq[:-1], self.seq[1:])])

hops = {}
locs = set()
for line in lines:
    a, b, d = re.findall("(.*) to (.*) = (\d+)", line)[0]
    hops[(a, b)] = int(d)
    hops[(b, a)] = int(d)
    locs.add(a)
    locs.add(b)

routes = [Route(route) for route in permutations(locs, len(locs))]

min_route = min(routes, key=len)
max_route = max(routes, key=len)

print(len(min_route))
print(len(max_route))
