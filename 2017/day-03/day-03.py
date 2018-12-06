with open('../data/04-input.txt', 'r') as f:
    phrases = f.read().splitlines()

def is_valid(pwd):
    pwd_split = pwd.strip().split(' ')
    pwd_uniq = set(pwd_split)
    return len(pwd_split) == len(pwd_uniq)

valid_phrases = [pwd for pwd in phrases if is_valid(pwd)]

print("::: PART A")
print(f"Number of Valid Passphrases: {len(valid_phrases)}\n")

#==============================================================================

def any_anagram(pwd):
    pwd_split = pwd.strip().split(' ')
    pwd_sorted = [''.join(sorted(w)) for w in pwd_split]
    pwd_standardized = ' '.join(pwd_sorted)
    return is_valid(pwd_standardized)

valid_phrases_b = [pwd for pwd in phrases if any_anagram(pwd)]

print("::: PART B")
print(f"Number of Valid Passphrases: {len(valid_phrases_b)}")
