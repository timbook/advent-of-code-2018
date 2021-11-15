import re
import itertools

with open('input.txt', 'r') as f:
    lines = f.readlines()

names = set([line.split()[0] for line in lines])
util = {name: {} for name in names}

for line in lines:
    pattern = "(.*) would (gain|lose) (\d+) happiness units by sitting next to (.*)."
    name, updown, n, nb = re.findall(pattern, line)[0]
    sign = 1 if updown == 'gain' else -1
    util[name][nb] = sign*int(n)

def evaluate_ordering(ordering):
    total = 0
    for i, name in enumerate(ordering):
        nb_l = ordering[(i - 1) % len(ordering)]
        nb_r = ordering[(i + 1) % len(ordering)]
        total += (util[name].get(nb_l, 0) + util[name].get(nb_r, 0))

    return total

values = [evaluate_ordering(ordering) for ordering in itertools.permutations(names, len(names))]

print(f"A ::: Maximum happiness: {max(values)}")

my_name = 'Tim'
names.add(my_name)
util[my_name] = {}
values = [evaluate_ordering(ordering) for ordering in itertools.permutations(names, len(names))]
print(f"B ::: Maximum happiness: {max(values)}")
