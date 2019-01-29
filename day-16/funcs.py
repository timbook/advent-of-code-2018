import copy
import re

class Sample:
    def __init__(self, before, instruction, after):
        self.before = Register(before)
        self.instruction = [int(i) for i in instruction.split(' ')]
        self.after = Register(after)
        self.op = self.instruction[0]

    def evaluate(self):
        self.valid_ops = []
        for opname, op in op_dict.items():
            if op(self.before, self.instruction) == self.after:
                self.valid_ops.append(opname)

class Register:
    def __init__(self, reg):
        if isinstance(reg, str):
            values = re.findall("\d+", reg)
            self.values = [int(v) for v in values]
        elif isinstance(reg, list):
            self.values = reg.copy()

    def __getitem__(self, i):
        return self.values[i]

    def __setitem__(self, key, value):
        self.values[key] = value

    def __eq__(self, r2):
        return self.values == r2.values

    def __repr__(self):
        return str(self.values)

def addr(reg_before, cmd):
    new_reg = Register(reg_before.values)
    new_reg[cmd[3]] = reg_before[cmd[1]] + reg_before[cmd[2]]
    return new_reg

def addi(reg_before, cmd):
    new_reg = Register(reg_before.values)
    new_reg[cmd[3]] = reg_before[cmd[1]] + cmd[2]
    return new_reg

def mulr(reg_before, cmd):
    new_reg = Register(reg_before.values)
    new_reg[cmd[3]] = reg_before[cmd[1]] * reg_before[cmd[2]]
    return new_reg

def muli(reg_before, cmd):
    new_reg = Register(reg_before.values)
    new_reg[cmd[3]] = reg_before[cmd[1]] * cmd[2]
    return new_reg

def banr(reg_before, cmd):
    new_reg = Register(reg_before.values)
    new_reg[cmd[3]] = reg_before[cmd[1]] & reg_before[cmd[2]]
    return new_reg

def bani(reg_before, cmd):
    new_reg = Register(reg_before.values)
    new_reg[cmd[3]] = reg_before[cmd[1]] & cmd[2]
    return new_reg

def borr(reg_before, cmd):
    new_reg = Register(reg_before.values)
    new_reg[cmd[3]] = reg_before[cmd[1]] | reg_before[cmd[2]]
    return new_reg

def bori(reg_before, cmd):
    new_reg = Register(reg_before.values)
    new_reg[cmd[3]] = reg_before[cmd[1]] | cmd[2]
    return new_reg

def setr(reg_before, cmd):
    new_reg = Register(reg_before.values)
    new_reg[cmd[3]] = reg_before[cmd[1]]
    return new_reg

def seti(reg_before, cmd):
    new_reg = Register(reg_before.values)
    new_reg[cmd[3]] = cmd[1]
    return new_reg

def gtir(reg_before, cmd):
    new_reg = Register(reg_before.values)
    new_reg[cmd[3]] = (cmd[1] > reg_before[cmd[2]]) * 1
    return new_reg

def gtri(reg_before, cmd):
    new_reg = Register(reg_before.values)
    new_reg[cmd[3]] = (reg_before[cmd[1]] > cmd[2]) * 1
    return new_reg

def gtrr(reg_before, cmd):
    new_reg = Register(reg_before.values)
    new_reg[cmd[3]] = (reg_before[cmd[1]] > reg_before[cmd[2]]) * 1
    return new_reg

def eqir(reg_before, cmd):
    new_reg = Register(reg_before.values)
    new_reg[cmd[3]] = (cmd[1] == reg_before[cmd[2]]) * 1
    return new_reg

def eqri(reg_before, cmd):
    new_reg = Register(reg_before.values)
    new_reg[cmd[3]] = (reg_before[cmd[1]] == cmd[2]) * 1
    return new_reg

def eqrr(reg_before, cmd):
    new_reg = Register(reg_before.values)
    new_reg[cmd[3]] = (reg_before[cmd[1]] == reg_before[cmd[2]]) * 1
    return new_reg

op_dict = {
    'addr': addr,
    'addi': addi,

    'mulr': mulr,
    'muli': muli,

    'banr': banr,
    'bani': bani,

    'borr': borr,
    'bori': bori,

    'setr': setr,
    'seti': seti,

    'gtir': gtir,
    'gtri': gtri,
    'gtrr': gtrr,

    'eqir': eqir,
    'eqri': eqri,
    'eqrr': eqrr
}
