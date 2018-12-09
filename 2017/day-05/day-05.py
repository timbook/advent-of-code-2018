with open('../data/05-input.txt', 'r') as f:
    jumps = f.read().splitlines()

jumps = [int(j) for j in jumps]

head = 0
n_steps = 0
while True:
    old_head = head
    try:
        head += jumps[old_head]
        jumps[old_head] += 1
        n_steps += 1
    except:
        break

print("::: PART A")
print(f"Number of Steps: {n_steps}\n")

#==============================================================================

with open('../data/05-input.txt', 'r') as f:
    jumps = f.read().splitlines()

jumps = [int(j) for j in jumps]

head = 0
n_steps = 0
while True:
    old_head = head
    try:
        head += jumps[old_head]

        if jumps[old_head] >= 3:
            jumps[old_head] -= 1
        else:
            jumps[old_head] += 1

        n_steps += 1
    except:
        break

print("::: PART B")
print(f"Number of Steps: {n_steps}")
