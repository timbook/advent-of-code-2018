import re

with open('input.txt', 'r') as f:
    lines = f.readlines()

#  lines = """Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
#  Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.""".split('\n')

class Deer:
    def __init__(self, line):
        pattern = "(.*) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds."
        name, v, t, rest = re.findall(pattern, line)[0]
        self.name = name
        self.v = int(v)
        self.t = int(t)
        self.rest = int(rest)

        self.dist = 0
        self.points = 0
        self.state = 'flying'
        self.t_remaining = self.t

    def __repr__(self):
        return f'{self.name}(v={self.v}, t={self.t}, rest={self.rest}, d={self.dist}, r_rem={self.t_remaining})'

    def tick(self):
        if self.state == 'flying':
            self.dist += self.v
            self.t_remaining -= 1

            if self.t_remaining == 0:
                self.state = 'resting'
                self.t_remaining = self.rest

        elif self.state == 'resting':
            self.t_remaining -= 1
            if self.t_remaining == 0:
                self.state = 'flying'
                self.t_remaining = self.t

    def tick_n(self, n):
        for _ in range(n):
            self.tick()

    def award_point(self):
        self.points += 1



deer = [Deer(line) for line in lines]

T = 2503
_ = [d.tick_n(T) for d in deer]

leader = max(deer, key=lambda d: d.dist)
print(f"A ::: The leader is {leader.name} at a distance of {leader.dist} km.")

deer = [Deer(line) for line in lines]
for _ in range(T):
    [d.tick() for d in deer]
    max_d = max(deer, key=lambda d: d.dist).dist
    deer_in_lead = [d for d in deer if d.dist == max_d]
    [d.award_point() for d in deer_in_lead]

leader = max(deer, key=lambda d: d.points)
print(f"B ::: The leader is {leader.name} with {leader.points} points.")
