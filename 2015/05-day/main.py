from string import ascii_lowercase as letters
import re

def cond1_a(s):
    return len(re.findall('[aeiou]', s.lower())) >= 3

def cond2_a(s):
    for c1, c2 in zip(s[:-1], s[1:]):
        if c1 == c2:
            return True
    return False

def cond3_a(s):
    return not any(['ab' in s, 'cd' in s, 'pq' in s, 'xy' in s])

def is_nice_a(s):
    return cond1_a(s) and cond2_a(s) and cond3_a(s)

with open('input.txt', 'r') as f:
    lines = f.readlines()

nice_strs = [is_nice_a(line.strip()) for line in lines]
n_nice = sum(nice_strs)

print('A :::')
print(f'There are {n_nice} nice strings')
print()

def cond1_b(s):
    pairs = [c1 + c2 for c1, c2 in zip(s[:-1], s[1:])]
    two_of_a_kinds = [pair for pair in pairs if s.count(pair) >= 2]
    return bool(two_of_a_kinds)

def cond2_b(s):
    return any([re.search(f'{char}[a-z]{char}', s) for char in letters])

def is_nice_b(s):
    return cond1_b(s) and cond2_b(s)

nice_strs = [is_nice_b(line.strip()) for line in lines]
n_nice = sum(nice_strs)

print('B :::')
print(f'There are {n_nice} nice strings')
print()
