with open('input.txt', 'r') as f:
    data = f.read()

ups = data.count('(')
downs = data.count(')')
print('A :::')
print(f'Final Floor = {ups - downs}')

floor = 0
for i, char in enumerate(data):
    floor += 1 if char == '(' else -1
    if floor < 0:
        break

print('B :::')
print(f'First Entered Basement at = {i + 1}')
