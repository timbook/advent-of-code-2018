import numpy as np

class Tracks:
    def __init__(self, data):
        self.grid = np.array([list(line) for line in data])

        grid_empty = self.grid.copy()
        grid_empty = np.where((grid_empty == '^') | (grid_empty == 'v'), '|', grid_empty)
        grid_empty = np.where((grid_empty == '>') | (grid_empty == '<'), '-', grid_empty)
        self.grid_empty = grid_empty

        row_up, col_up = np.where(self.grid == '^')
        row_down, col_down = np.where(self.grid == 'v')
        row_left, col_left = np.where(self.grid == '<')
        row_right, col_right = np.where(self.grid == '>')

        carts = \
            list(zip(row_up, col_up)) + \
            list(zip(row_down, col_down)) + \
            list(zip(row_left, col_left)) + \
            list(zip(row_right, col_right))

        carts = [(r, c, self.grid[r, c]) for r, c in carts]

        self.carts = [Cart(*cart, self) for cart in carts]
        self.sort_carts()


    def advance_carts(self):
        self.sort_carts()
        for cart in self.carts:
            cart.advance()
            if self.check_for_crashes():
                return True
        return False

    def sort_carts(self):
        self.carts.sort(key=lambda c: (c.row, c.col)) 

    def advance_and_drop(self):
        self.sort_carts()
        for cart in self.carts:
            cart.advance()
            self.check_for_crash_and_drop()
            if len(self.carts) == 1:
                return True
        return False

    def check_for_crash_and_drop(self):
        cart_tuples = [c.as_tuple() for c in self.carts]
        for cart_tuple in set(cart_tuples):
            if cart_tuples.count(cart_tuple) > 1:
                self.carts = [c for c in self.carts if (c.row, c.col) != (cart_tuple[0], cart_tuple[1])]

    def check_for_crashes(self):
        cart_tuples = [c.as_tuple() for c in self.carts]
        duplicates = [c for c in cart_tuples if cart_tuples.count(c) > 1]
        if duplicates:
            self.crash_site = set(duplicates)
        return len(cart_tuples) != len(set(cart_tuples))

class Cart:
    def __init__(self, row, col, sym, tracks):
        self.row = row
        self.col = col
        self.sym = sym
        self.status = 0
        self.tracks = tracks

    def __repr__(self):
        return f"(Cart({self.row}, {self.col}, {self.sym}))"

    def as_tuple(self):
        return (self.row, self.col)

    def advance(self):

        # GOING NORTH
        if self.sym == '^':
            turn_rule = ['<', '^', '>']
            next_spot = self.tracks.grid_empty[self.row - 1, self.col]

            if next_spot == '\\':
                self.sym = '<'
            elif next_spot == '/':
                self.sym = '>'
            elif next_spot == '+':
                self.sym = turn_rule[self.status]
                self.status = (self.status + 1) % 3

            self.row -= 1

        # GOING EAST
        elif self.sym == '>':
            turn_rule = ['^', '>', 'v']
            next_spot = self.tracks.grid_empty[self.row, self.col + 1]
            
            if next_spot == '\\':
                self.sym = 'v'
            elif next_spot == '/':
                self.sym = '^'
            elif next_spot == '+':
                self.sym = turn_rule[self.status]
                self.status = (self.status + 1) % 3

            self.col += 1

        # GOING SOUTH
        elif self.sym == 'v':
            turn_rule = ['>', 'v', '<']
            next_spot = self.tracks.grid_empty[self.row + 1, self.col]

            if next_spot == '\\':
                self.sym = '>'
            elif next_spot == '/':
                self.sym = '<'
            elif next_spot == '+':
                self.sym = turn_rule[self.status]
                self.status = (self.status + 1) % 3

            self.row += 1

        # GOING WEST
        elif self.sym == '<':
            turn_rule = ['v', '<', '^']
            next_spot = self.tracks.grid_empty[self.row, self.col - 1]

            if next_spot == '\\':
                self.sym = '^'
            elif next_spot == '/':
                self.sym = 'v'
            elif next_spot == '+':
                self.sym = turn_rule[self.status]
                self.status = (self.status + 1) % 3

            self.col -= 1
