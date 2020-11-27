with open('input.txt', 'r') as f:
    raw = f.read().strip()

class Hex:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def move(self, direction):
        if direction == 'n':
            self.y += 1
            self.z -= 1
        elif direction == 'ne':
            self.x += 1
            self.z -= 1
        elif direction == 'se':
            self.x += 1
            self.y -= 1
        elif direction == 's':
            self.y -= 1
            self.z += 1
        elif direction == 'sw':
            self.x -= 1
            self.z += 1
        elif direction == 'nw':
            self.x -= 1
            self.y += 1

    def distance(self, x=0, y=0, z=0):
        return int((abs(self.x - x) + abs(self.y - y) + abs(self.z - z)) / 2)

    def process_data(self, data):
        max_d = -1
        for direction in data:
            self.move(direction)
            d = self.distance()
            max_d = d if d > max_d else max_d

        self.max_d = max_d

data = raw.split(',')
child = Hex()
child.process_data(data)
distance = child.distance()
print(f'The child is {distance} steps away.')
print(f'He only ever got a maximum of {child.max_d} away!')
