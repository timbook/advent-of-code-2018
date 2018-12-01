with open("data/01-input.txt", 'r') as f:
    lines = f.readlines()

items = [int(n.strip()) for n in lines]

print(sum(items))
