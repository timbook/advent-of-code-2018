from funcs import op_dict, Sample, Register
import re

with open("../data/16A-input.txt") as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]
lines = [line for line in lines if line]

samples = []
while lines:
    before, instruction, after = lines[:3]
    new_sample = Sample(before, instruction, after)
    samples.append(new_sample)
    lines = lines[3:]

for sample in samples:
    sample.evaluate()

opcodes_like = [len(sample.valid_ops) for sample in samples]
n_valid_gt_3 = sum(ops >= 3 for ops in opcodes_like)

print("::: PART A")
print(f"NUMBER OF INSTRUCTIONS WITH 3 OR MORE VALID OP CODES: {n_valid_gt_3}\n")

# ============================================================================

op_samples = []
for i in range(16):
    op_i = [s for s in samples if s.op == i]
    op_sets = [set(s.valid_ops) for s in op_i]
    op_samples.append((i, set.intersection(*op_sets)))

known_ops = {}
remaining_ops = list(op_dict.keys()).copy()

while remaining_ops:
    for (i, op_set) in op_samples:
        op_possible = op_set.intersection(set(remaining_ops))
        if len(op_possible) == 1:
            op_name = [o for o in op_possible][0]
            if op_name in remaining_ops:
                known_ops[i] = op_name
                remaining_ops.remove(op_name)

    op_samples = [(i, ops) for i, ops in op_samples if not known_ops.get(i)]

actions = [s.instruction for s in samples]

with open("../data/16B-input.txt") as f:
    actions = f.readlines()

def to_int(action):
    action_list = action.split(' ')
    return [int(a) for a in action_list]

actions = [to_int(action) for action in actions]

state = Register([0, 0, 0, 0])
for action in actions:
    op = op_dict[known_ops[action[0]]]
    state = op(state, action)

print(state)

print("::: PART B")
print(f"THE VALUE OF REGISTER 0 IS: {state[0]}")
