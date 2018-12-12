import re

with open('../data/12-input.txt', 'r') as f:
    data = f.read().splitlines()

state_input = re.findall('initial state: (.*)', data[0])[0]
state = {i:st for i, st in enumerate(state_input)}
init_state = state.copy()

rule_lines = data[2:]
rules = {line[:5]:line[-1] for line in rule_lines}

def get_situation(pot, state):
    pots = [pot - 2, pot - 1, pot, pot + 1, pot + 2]
    situation = ''.join([state.get(p, '.') for p in pots])
    return situation

def run_sim(n_gen, state):
    for gen in range(n_gen):

        min_pot = min(state.keys())
        max_pot = max(state.keys())
        state[min_pot - 2] = '.'
        state[min_pot - 1] = '.'
        state[max_pot + 1] = '.'
        state[max_pot + 2] = '.'

        state = {pot:rules[get_situation(pot, state)] for pot in state.keys()}

    total = 0
    for pot, value in state.items():
        if value == '#':
            total += pot

    return total

total_20 = run_sim(20, state)

print("::: PART A")
print(f"Total after 20 generations: {total_20}\n")

#==============================================================================

print("::: PART B")
print(f"Total after 50B generations: {50_000_000_000 * 800}")
