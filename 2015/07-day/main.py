import re

with open('input.txt', 'r') as f:
    lines = f.readlines()

wires_done = set()

def str_to_value(s):
    if s.isdigit():
        return int(s)
    else:
        return wire_map[s].value

def parents_satisfied(wire):
    parents = [parent for parent in wire.parents if parent.isalpha()]
    return all(parent in wires_done for parent in parents)

op_map = {
    'AND': lambda a, b: a & b,
    'OR': lambda a, b: a | b,
    'LSHIFT': lambda a, b: a << b,
    'RSHIFT': lambda a, b: a >> b
}

class Wire:
    def __init__(self, instruction):
        lhs, rhs = re.findall("(.*) -> (\w+)", instruction.strip())[0]

        self.lhs = lhs
        self.name = rhs
        self.value = None

        # Number -> Assign!
        if re.search("^\d+$", lhs):
            self.value = int(lhs)
            self.parents = []
            wires_done.add(self.name)

        elif re.search("^[a-z]+$", lhs):
            self.parents = [lhs]

        # Unary Operators
        elif re.search("NOT", lhs):
            self.parents = re.findall("NOT (\w+)", lhs)

        # Binary Operators
        elif re.search("(AND|OR|LSHIFT|RSHIFT)", lhs):
            self.parents = re.findall("(\w+) \w+ (\w+)", lhs)[0]

    def execute(self):
        if re.search("NOT", self.lhs):
            predicate = str_to_value(self.parents[0])
            self.value = ~predicate
        elif re.search("(AND|OR|LSHIFT|RSHIFT)", self.lhs):
            op_str = re.findall("(AND|OR|LSHIFT|RSHIFT)", self.lhs)[0]
            op = op_map[op_str]
            v1 = str_to_value(self.parents[0])
            v2 = str_to_value(self.parents[1])
            self.value = op(v1, v2)
        elif re.search("^[a-z]+$", self.lhs):
            self.value = wire_map[self.lhs].value

        wires_done.add(self.name)

wires = [Wire(line) for line in lines]
wire_map = {wire.name:wire for wire in wires}

for i in range(200):
    for wire in wires:

        if parents_satisfied(wire):
            wire.execute()

    if 'a' in wires_done:
        break

    n = len(wires_done)

a_val = wire_map['a'].value
print('A :::')
print(f"The value of wire a: {a_val}")
print()

wires = [Wire(line) for line in lines]
wire_map = {wire.name:wire for wire in wires}
wire_map['b'].value = a_val
wires_done = {'b'}

for i in range(200):
    for wire in wires:

        if parents_satisfied(wire):
            wire.execute()

    if 'a' in wires_done:
        break

    n = len(wires_done)

a_val = wire_map['a'].value
print('B :::')
print(f"The value of wire a: {a_val}")










