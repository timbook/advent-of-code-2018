with open('data/02-input.txt', 'r') as f:
    data = f.read().splitlines()

def has_grp(text, n):
    letters = set(text)
    return any(text.count(char) == n for char in letters)

pairs = [s for s in data if has_grp(s, 2)]
triples = [s for s in data if has_grp(s, 3)]

n_pairs = len(pairs)
n_triples = len(triples)

print(n_pairs * n_triples)
