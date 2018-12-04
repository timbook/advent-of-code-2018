import re
from items import get_guard_num, get_min, get_cycle, SleepMatrix

with open('../data/04-input.txt', 'r') as f:
    records = f.read().splitlines()

records.sort()

guard_rx = re.compile('#[0-9]+')

guards = [guard_rx.findall(rec)[0] for rec in records if re.search(guard_rx, rec)]
n_guards = len(set(guards))

sleep_mx = SleepMatrix(n_guards, 60, guards)

for rec in get_cycle(records):
    sleep_mx.process_shift(rec)

sleepiest_guard = int(sleep_mx.sleepiest_guard().replace('#', ''))
sleepiest_minute = sleep_mx.sleepiest_minute()

print("::: PART A")
print(f"Sleepiest Guard: {sleepiest_guard}")
print(f"Sleepiest Minute for that Guard: {sleepiest_minute}")
print(f"{sleepiest_guard * sleepiest_minute}\n")

#==============================================================================

worst_guard, best_minute = sleep_mx.get_best_combo()
worst_guard = int(worst_guard.replace('#', ''))

print("::: PART B")
print(f"Worst Guard: {worst_guard}")
print(f"Best Minute: {best_minute}")
print(f"Best Combo Product: {worst_guard * best_minute}")
