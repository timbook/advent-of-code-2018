from itertools import combinations

with open('../data/02-input.txt', 'r') as f:
    data = f.read().splitlines()

def has_grp(text, n):
    letters = set(text)
    return any(text.count(char) == n for char in letters)

pairs = [s for s in data if has_grp(s, 2)]
triples = [s for s in data if has_grp(s, 3)]

n_pairs = len(pairs)
n_triples = len(triples)

print("::: PART A")
print(f"CHECKSUM: {n_pairs * n_triples}\n")

# =============================================================================

def has_one_diff(s1, s2):
    diff_count = 0

    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            diff_count += 1

    return diff_count == 1

def letters_in_common(s1, s2):
    str_out = ""

    for c1, c2 in zip(s1, s2):
        if c1 == c2:
            str_out += c1

    return str_out

box_ids = [pair for pair in combinations(data, 2) if has_one_diff(*pair)][0]

print("::: PART B")
print(f"LETTERS IN COMMON: {letters_in_common(*box_ids)}")
