from collections import deque

#  raw = """0: 3
#  1: 2
#  4: 4
#  6: 4""".strip().split('\n')

with open('input.txt', 'r') as f:
    raw = f.read()
    raw = [line for line in raw.strip().split('\n')]

class Layer:
    def __init__(self, depth, range_, thickness=1):
        self.depth = depth
        self.range = range_
        self.thickness = thickness
        self.wall = deque([1] + [0]*(self.range - 1))
        self.direction = 1

    def tick(self):
        if self.wall[0] == 1:
            self.direction = 1
        elif self.wall[-1] == 1:
            self.direction = -1
        self.wall.rotate(self.direction)

    def at_zero(self):
        return self.wall[0] == 1

    def severity(self):
        return self.depth*self.range

class Firewall:
    def __init__(self, data):
        self.loc = -1
        self.layers = {}
        self.process_data(data)
        self.severity = 0
        self.ever_caught = False

    def process_data(self, data):
        for line in data:
            d, r = line.split(': ')
            self.layers[int(d)] = Layer(int(d), int(r))

    def move(self):
        self.loc += 1

    def check_if_caught(self):
        caught = self.loc in self.layers and self.layers[self.loc].at_zero()
        if caught:
            self.severity += self.layers[self.loc].severity()
            self.ever_caught = True
        return caught

    def tick(self):
        [layer.tick() for _, layer in self.layers.items()]

    def step(self):
        self.move()
        self.check_if_caught()
        self.tick()

    def run(self, quit_if_caught=False):
        for i in range(max(self.layers.keys()) + 1):
            firewall.step()
            if quit_if_caught and self.ever_caught:
                return

    def delay(self, picoseconds):
        for _ in range(picoseconds):
            self.tick()

firewall = Firewall(raw)
firewall.run()

print(f"Severity of route: {firewall.severity}")

delay = 39_000
while True:
    firewall = Firewall(raw)
    firewall.delay(delay)
    firewall.run(quit_if_caught=True)
    if not firewall.ever_caught:
        break
    else:
        delay += 1
        if delay % 1000 == 0:
            print(f"Passing delay = {delay} and not done...")
    
print(f"The first delay to avoid detection is {delay}")
