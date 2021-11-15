import re
from itertools import permutations

with open('input.txt', 'r') as f:
    lines = f.readlines()

class Hop:
    def __init__(self, line):
        a, b, d = re.findall("(.*) to (.*) = (\d+)", line)[0]
        self.a = a
        self.b = b
        self.d = int(d)

    def __repr__(self):
        return f"({self.a}, {self.b}) => {self.d}"

    def find(self, a, b):
        return {self.a, self.b} == {a, b}

class Route:
    def __init__(self, seq):
        self.seq = seq

    def __len__(self):
        total = 0
        for a, b in zip(self.seq[:-1], self.seq[1:]):
            hop = find_hop(a, b)
            total += hop.d
        return total

def find_hop(a, b):
    return [hop for hop in hops if hop.find(a, b)][0]

hops = [Hop(line) for line in lines]
locs = set([hop.a for hop in hops] + [hop.b for hop in hops])

routes = []
for route in permutations(locs, len(locs)):
    routes.append(Route(route))

min_route = min(routes, key=len)
max_route = max(routes, key=len)

print(len(min_route))
print(len(max_route))
