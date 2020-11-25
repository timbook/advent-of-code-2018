import re

with open('input.txt', 'r') as f:
    raw = f.readlines()

OP_MAP = {
    '<': lambda a, b: a < b,
    '<=': lambda a, b: a <= b,
    '>': lambda a, b: a > b,
    '>=': lambda a, b: a >= b,
    '==': lambda a, b: a == b,
    '!=': lambda a, b: a != b
}

class Instruction:
    def __init__(self, raw):
        values = raw.split()
        self.operand, self.op, self.value = values[:3]
        self.cond_operand, self.cond_op, self.cond_value = values[-3:]

        self.value = int(self.value)
        self.cond_value = int(self.cond_value)

    def operate(self, register):
        if OP_MAP[self.cond_op](register.get(self.cond_operand, 0), self.cond_value):
            mult = 1 if self.op == 'inc' else -1
            register[self.operand] = register.get(self.operand, 0) + mult*self.value

        return register[self.operand]


instructions = [Instruction(line) for line in raw]

register = {instruction.operand: 0 for instruction in instructions}

historical_values = []
for instruction in instructions:
    historical_values.append(instruction.operate(register))

largest_key = max(register, key=register.get)
largest_value = register[largest_key]
print(f'Largest value exists at: ({largest_key}, {largest_value})')

largest_in_history = max(historical_values)
print(f'Largest value in process history: {largest_in_history}')
