with open('input.txt', 'r') as f:
    lines = f.readlines()

dims = [line.strip().split('x') for line in lines]
dims = [(int(dim[0]), int(dim[1]), int(dim[2])) for dim in dims]

totals_per_package = [
    2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)
    for (l, w, h) in dims
]

total = sum(totals_per_package)
print('A :::')
print(f'Total wrapping paper needed = {total}')
print()

total_ribbon_per_package = [
    2*min(l + w, w + h, l + h) + l*w*h
    for (l, w, h) in dims
]

total_ribbon = sum(total_ribbon_per_package)
print('B :::')
print(f'Total ribbon needed = {total}')
