from collections import deque
import numpy as np

dancers = 'abcdefghijklmnop'

with open('input.txt', 'r') as f:
    instructions  = f.read().split(',')

# PART 1 ======================================================================

class Troupe:
    def __init__(self, dancers):
        self.dancers = deque(dancers)

    def process_move(self, instruction):
        move = instruction[0]
        predicate = instruction[1:]

        if move == 's':
            self.spin(predicate)
        elif move == 'x':
            self.exchange(predicate)
        elif move == 'p':
            self.partner(predicate)

    def process_move_set(self, instructions):
        for instruction in instructions:
            self.process_move(instruction)

    def spin(self, dist):
        self.dancers.rotate(int(dist))

    def exchange(self, predicate):
        loc1, loc2 = predicate.split('/')
        loc1, loc2 = int(loc1), int(loc2)

        temp = self.dancers[loc1]
        self.dancers[loc1] = self.dancers[loc2]
        self.dancers[loc2] = temp

    def partner(self, predicate):
        d1, d2 = predicate.split('/')
        loc1 = self.dancers.index(d1)
        loc2 = self.dancers.index(d2)
        self.dancers[loc2] = d1
        self.dancers[loc1] = d2

    def show(self):
        return ''.join(self.dancers)

troupe = Troupe(dancers)
troupe.process_move_set(instructions)
dancers_final = troupe.show()

print(f"The final orientation of dancers is: {dancers_final}")

# PART 2 ======================================================================

dancers_init = dancers
dancers_final = troupe.show()

letter_map = {letter:number for number, letter in enumerate(dancers_init)}
move_map = np.array([letter_map[letter] for letter in dancers_final])

dancers_array = np.array(list(dancers))
for i in range(1_000_000):
    dancers_array = dancers_array[move_map]

dancers_million = ''.join(list(dancers_array))
print(f"After a million moves: {dancers_million}")

move_map_million = np.array([letter_map[letter] for letter in dancers_million])

dancers_array = np.array(list(dancers))
print(dancers_array)
for i in range(1_000):
    dancers_array = dancers_array[move_map_million]
    condensed = ''.join(list(dancers_array))
    print(f"Iter {i}: {condensed}")

dancers_billion = ''.join(list(dancers_array))

print(f"After a billion moves: {dancers_billion}")
