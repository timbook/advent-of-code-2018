class Route:
    def __init__(self, steps):
        self.steps = steps
        self.state = (0, 0)
        self.history = [(0, 0)]

    def move(self, step):
        x_move, y_move = 0, 0
        if step == '>':
            x_move = 1
        elif step == '<':
            x_move = -1
        elif step == '^':
            y_move = 1
        elif step == 'v':
            y_move = -1

        self.state = (self.state[0] + x_move, self.state[1] + y_move)
        self.history.append(self.state)

    def run_route(self):
        for step in self.steps:
            self.move(step)

with open('input.txt', 'r') as f:
    data = f.read().strip()

r = Route(data)
r.run_route()
n_homes = len(set(r.history))

print('A :::')
print(f'Number of homes visited = {n_homes}')
print()

r1 = Route(data[::2])
r2 = Route(data[1::2])

r1.run_route()
r2.run_route()

routes = set(r1.history + r2.history)
n_homes = len(routes)
print('B :::')
print(f'Number of homes visited = {n_homes}')
