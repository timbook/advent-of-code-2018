with open('../data/01-input.txt', 'r') as f:
    data = f.read().strip()

datap1 = data + data[0]

total = 0
for i, value in enumerate(datap1[:-1]):
    if datap1[i] == datap1[i + 1]:
        total += int(value)

print("::: PART A")
print(f"CAPTCHA SOLUTION: {total}\n")

#==============================================================================

full_step = len(data)
half_step = int(len(data) / 2)

total = 0
for i, value in enumerate(data):
    future_index = (i + half_step) % full_step
    if data[i] == data[future_index]:
        total += int(value)

print("::: PART B")
print(f"CAPTCHA SOLUTION: {total}")
