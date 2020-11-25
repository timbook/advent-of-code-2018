from functools import reduce
import numpy as np

input_str = '14,58,0,116,179,16,1,104,2,254,167,86,255,55,122,244'

# PART 1 ======================================================================

lengths = [int(i) for i in input_str.split(',')]
arr = np.arange(256)

def print_arr(arr):
    print(''.join([str(x) for x in arr]))

def knot_round(arr, pointer=0, skip=0):
    n = len(arr)

    for l in lengths:
        ix = np.arange(pointer, pointer + l) % n
        arr[ix] = arr[ix][::-1]
        pointer += (l + skip) % n
        skip += 1

    return arr, pointer, skip

arr_out, _, _ = knot_round(arr)
solution = arr_out[0]*arr_out[1]
print(f'Product of first two numbers: {solution}')

# PART 2 ======================================================================
lengths = [ord(c) for c in input_str]
lengths.extend([17, 31, 73, 47, 23])

arr = np.arange(256)
pointer = 0
skip = 0
for _ in range(64):
    arr, pointer, skip = knot_round(arr, pointer, skip)

sparse_hash = ''
ix = np.arange(256) // 16
xor = lambda a, b: a ^ b
to_hex_str = lambda n: hex(n)[2:].rjust(2, '0')

for i in range(16):
    hash_num = reduce(xor, arr[ix == i])
    hash_hex = to_hex_str(hash_num)
    sparse_hash += hash_hex

print(f'Resulting hash: {sparse_hash}')
