# Part A ======================================================================
class Generator:
    def __init__(self, start, factor):
        self.value = start
        self.factor = factor

    def run(self):
        self.value = self.value * self.factor % 2147483647

    @property
    def tail(self):
        return bin(self.value)[-16:].replace('0b', '')

factor_a = 16807
factor_b = 48271

#  start_a = 65
#  start_b = 8921
start_a = 722
start_b = 354

gen_a = Generator(start_a, factor_a)
gen_b = Generator(start_b, factor_b)

count = 0
for i in range(40_000_000):
    if i % 1_000_000 == 0:
        print(i)
    gen_a.run()
    gen_b.run()
    if gen_a.tail == gen_b.tail:
        count += 1

print(count)
