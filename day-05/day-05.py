with open('../data/05-input.txt', 'r') as f:
    chain = f.read().strip()

chain = list(chain)

def is_reactive(char1, char2):
    return (char1.lower() == char2.lower()) and (char1 != char2)

def reduce_polymer(chain):

    polymer = chain.copy()

    while True:
        startlen = len(polymer)

        for i, unit in enumerate(polymer[:-1]):
            if is_reactive(polymer[i], polymer[i + 1]):
                polymer.pop(i)
                polymer.pop(i)
                break

        endlen = len(polymer)

        if startlen == endlen:
            break

    return len(polymer)

print("::: PART A")
print(f"Finishing Length: {reduce_polymer(chain)}\n")

#==============================================================================

letters = list('abcdefghijklmnopqrstuvwxyz')

def drop_unit(chain, unit):
    chainstr = ''.join(chain)
    chainstr = chainstr.replace(unit.lower(), '').replace(unit.upper(), '')
    return list(chainstr)

reduction_dict = {
    char: reduce_polymer(drop_unit(chain, char))
    for char in letters
}

remains = list(reduction_dict.values())

print("::: PART B")
print(f"SOLUTION: {min(remains)}")







