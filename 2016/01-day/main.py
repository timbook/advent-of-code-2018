from collections import deque

with open('input.txt', 'r') as f:
    data = f.read().strip().split(",")

class Person:
    def __init__(self):
        self.x, self.y = (0, 0)
        self.direction = deque(['N', 'E', 'S', 'W'])
        self.visited = {(0, 0)}
        self.no_double_visits = True

    def process_move(self, move):
        turn = move.strip()[0]
        dist = int(move.strip()[1:])
        rot = -1 if turn == 'R' else 1
        self.direction.rotate(rot)

        if self.direction[0] == 'N':
            new_locs = [(self.x, self.y + i + 1) for i in range(dist)]
            self.y += dist
        elif self.direction[0] == 'S':
            new_locs = [(self.x, self.y - i - 1) for i in range(dist)]
            self.y -= dist
        elif self.direction[0] == 'E':
            new_locs = [(self.x + i + 1, self.y) for i in range(dist)]
            self.x += dist
        elif self.direction[0] == 'W':
            new_locs = [(self.x - i - 1, self.y) for i in range(dist)]
            self.x -= dist

        if self.no_double_visits:
            for loc in new_locs:
                if loc in self.visited:
                    self.double_visit = loc
                    self.no_double_visits = False
                else:
                    self.visited.add(loc)

me = Person()
for move in data:
    me.process_move(move)

final_dist = abs(me.x) + abs(me.y)
print(f"A ::: Final Distance = {final_dist}")

hq_loc = me.double_visit
hq_dist = abs(hq_loc[0]) + abs(hq_loc[1])

print(f"B ::: Easter Bunny HQ = {hq_dist}")
