import re
from collections import deque

data = "466 players; last marble is worth 71436 points"

rx = "([0-9]+) players; last marble is worth ([0-9]+) points"
n_players, max_points = re.findall(rx, data)[0]
n_players = int(n_players)
max_points = int(max_points)

def run_game(n_players, max_points):
    point_dict = {k: 0 for k in range(n_players)}

    circle = deque([0, 1], maxlen=max_points)
    current = 1
    player = 0

    mod_circle = lambda n: n % len(circle)
    mod_player = lambda n: n % n_players

    for m in range(2, max_points + 1):

        if m % 10_000_000 == 0:
            print(f"Round {m}")

        if m % 23 != 0:
            circle.rotate(2)
            circle.append(m)
        else:
            circle.rotate(-7)
            point_dict[player] += m + circle.pop()

        player = mod_player(player + 1)

    return point_dict

scores = run_game(n_players, max_points)

winning_points = max(v for k, v in scores.items())

print("::: PART A")
print(f"High score: {winning_points}\n")

#==============================================================================

scores = run_game(n_players, 100*max_points)
winning_points = max(v for k, v in scores.items())

print("::: PART B")
print(f"High score: {winning_points}")
