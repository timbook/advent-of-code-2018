import re

lines_raw = open('input.txt', 'r').readlines()
lines = [re.split('\[|\]', l.strip()) for l in lines_raw]

def is_abba(s):
    return s[:2] == s[2:][::-1] and s[:2] != s[2:]

def has_abba(s):
    L = len(s)

    if L == 4:
        return is_abba(s)

    for i in range(L - 4):
        s_sub = s[i:(i + 4)]
        if is_abba(s_sub):
            return True

    return False

def is_valid(line):
    out_bracket = [s for i, s in enumerate(line) if i % 2 == 0]
    out_bracket_ok = any([has_abba(s) for s in out_bracket])

    in_bracket = [s for i, s in enumerate(line) if i % 2 == 1]
    in_bracket_ok = not any([has_abba(s) for s in in_bracket])

    #  import pdb; pdb.set_trace()

    return out_bracket_ok and in_bracket_ok


# Not 77 or 112 or 109
valid_tls = [is_valid(l) for l in lines]
print(sum(valid_tls))
