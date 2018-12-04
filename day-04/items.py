import re
import numpy as np

def get_guard_num(rec):
    rx = re.compile('#[0-9]+')
    return int(rx.findall(rec)[0].replace('#', ''))

def get_min(rec):
    rx = re.compile(':[0-9]{2}')
    return int(rx.findall(rec)[0].replace(':', ''))

def get_cycle(recs):
    gid = 0
    for rec in recs:
        if re.search('begins shift', rec):
            gid = get_guard_num(rec)
        if re.search('falls asleep', rec):
            sleep_index = get_min(rec)
        if re.search('wakes up', rec):
            awake_index = get_min(rec)
            yield (gid, sleep_index, awake_index)

class SleepMatrix:
    def __init__(self, n, p, guards):
        self.mx = np.zeros((n, p))
        self.guards = list(set(guards))

    def process_shift(self, record):
        gid, sleep_index, awake_index = record
        row = self.guards.index(f"#{gid}")
        self.mx[row, sleep_index:awake_index] += 1

    def sleepiest_guard(self):
        guard_laziness = np.sum(self.mx, axis=1)
        sleepiest_index = np.argmax(guard_laziness)
        return self.guards[sleepiest_index]

    def sleepiest_minute(self):
        sleepiest_guard = self.sleepiest_guard()
        row = self.guards.index(sleepiest_guard)
        schedule = self.mx[row, :]
        return np.argmax(schedule)

    def get_best_combo(self):
        max_where = (self.mx == np.max(self.mx))
        max_row = np.argmax(np.sum(max_where, axis=1))
        max_col = np.argmax(np.sum(max_where, axis=0))
        worst_guard = self.guards[max_row]
        return worst_guard, max_col
