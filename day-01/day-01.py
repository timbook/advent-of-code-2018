import sys

with open("data/01-input.txt", 'r') as f:
    lines = f.readlines()

items = [int(n.strip()) for n in lines]

print(f"Part 1 Answer: {sum(items)}")

record = set()
freq = 0
done = False
while True:
    for i in items:
        freq += i
        if freq in record:
            print(f"Part 2 Answer: {freq}")
            sys.exit(0)
        else:
            record.add(freq)

