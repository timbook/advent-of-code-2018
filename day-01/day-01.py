import sys
import os

with open("../data/01-input.txt", 'r') as f:
    lines = f.readlines()

items = [int(n.strip()) for n in lines]

print("::: PART A")
print(f"FREQUENCY: {sum(items)}\n")

record = set()
freq = 0
done = False
while True:
    for i in items:
        freq += i
        if freq in record:
            print("::: PART B")
            print(f"FREQUENCY: {freq}")
            sys.exit(0)
        else:
            record.add(freq)

