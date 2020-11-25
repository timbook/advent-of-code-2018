import numpy as np

data_raw = '10	3	15	10	5	15	5	15	9	2	5	8	5	2	3	6'
data = [int(x) for x in data_raw.split('\t')]

class MemoryBank:
    def __init__(self, data):
        self.data = data
        self.cache = []

    def reallocate(self):
        val = max(self.data)
        loc = self.data.index(val)
        self.data[loc] = 0
        
        while val > 0:
            loc = (loc + 1) % len(self.data)
            self.data[loc] += 1
            val -= 1

        return ''.join([str(x) for x in self.data])

    def add_state(self, entry):
        self.cache.append(entry)

    def query_cache(self, entry):
        return entry in self.cache

    def run_routine(self):

        while True:
            state = self.reallocate()
            if self.query_cache(state):
                self.add_state(state)
                self.offending_state = state
                break
            self.add_state(state)

    def get_cycle_len(self):
        data_vec = np.array(self.cache)
        locs = np.where(data_vec ==  self.offending_state)[0]
        return locs[1] - locs[0]

bank = MemoryBank(data)
bank.run_routine()
print(f'Length of bank: {len(bank.cache)}')
cycle_len = bank.get_cycle_len()
print(f'Cycle length: {cycle_len}')
