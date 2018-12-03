from items import FabricBoard, Claim
from itertools import combinations

with open('../data/03-input.txt', 'r') as f:
    input_lines = f.read().splitlines()

fb = FabricBoard()

for line in input_lines:
    cl = Claim(line)
    fb.add_claim(cl)

print("::: PART A")
print(f"The number of overlapping squares: {fb.get_overlapping_squares()}\n")

#==============================================================================

solo_claim = ""
for line in input_lines:
    cl = Claim(line)
    fb.rm_claim(cl)
    if fb.check_empty(cl):
        solo_claim = cl.claim_id
        break
    else:
        fb.add_claim(cl)
    
print("::: PART B")
print(f"The only claim that does not over lap is: {solo_claim}")
