with open('input.txt', 'r') as f:
    lines = f.readlines()

class NumPad:
    def __init__(self):
        self.grid = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        self.x, self.y = (1, 1)

    def move(self, m):
        if m == 'U':
            self.y = max(self.y - 1, 0)
        elif m == 'D':
            self.y = min(self.y + 1, 2)
        elif m == 'L':
            self.x = max(self.x - 1, 0)
        elif m == 'R':
            self.x = min(self.x + 1, 2)

    def get(self):
        return self.grid[self.y][self.x]

pad = NumPad()

password = ''
for line in lines:
    for char in line.strip():
        pad.move(char)
    password += str(pad.get())

print(f"A ::: Password = {password}")

class NumPadB:
    def __init__(self):
        self.grid = [
            ['X', 'X', '1', 'X', 'X'],
            ['X', '2', '3', '4', 'X'],
            ['5', '6', '7', '8', '9'],
            ['X', 'A', 'B', 'C', 'X'],
            ['X', 'X', 'D', 'X', 'X']
        ]
        self.x, self.y = (0, 2)

    def check_legal(self, x, y):
        return self.grid[y][x] != 'X'

    def move(self, m):
        if m == 'U':
            new_y = max(self.y - 1, 0)
            self.y = new_y if self.check_legal(self.x, new_y) else self.y
        elif m == 'D':
            new_y = min(self.y + 1, 4)
            self.y = new_y if self.check_legal(self.x, new_y) else self.y
        elif m == 'L':
            new_x = max(self.x - 1, 0)
            self.x = new_x if self.check_legal(new_x, self.y) else self.x
        elif m == 'R':
            new_x = min(self.x + 1, 4)
            self.x = new_x if self.check_legal(new_x, self.y) else self.x

    def get(self):
        return self.grid[self.y][self.x]

padb = NumPadB()
password = ''
for line in lines:
    for char in line.strip():
        padb.move(char)
    password += str(padb.get())

print(f"B ::: Password = {password}")
