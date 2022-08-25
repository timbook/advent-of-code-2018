import re
import pandas as pd
from string import ascii_lowercase as letters

with open('input.txt', 'r') as f:
    lines = f.readlines()

def process_room(line):
    name_encrypted = re.findall('([\w-]+)-\d', line)[0]
    num = re.findall('\d+', line)[0]
    checksum = re.findall('\[(\w{5})\]', line)[0]
    return name_encrypted, num, checksum
    
def check_room(room):
    s = pd.Series(list(room[0].replace('-', '')))
    df = s.value_counts().to_frame().reset_index()
    df.columns = ['letter', 'freq']
    checksum_truth = ''.join(df.sort_values(['freq', 'letter'], ascending=[False, True]).head().letter.to_list())
    return int(room[1]) if checksum_truth == room[2] else 0

rooms = [process_room(line) for line in lines]
real_ids = [check_room(room) for room in rooms]

print(f"A ::: Sum of Sector IDs of real rooms = {sum(real_ids)}")

def decrypt_letter(char, n):
    if char == '-':
        return ' '
    else:
        return letters[(letters.index(char) + int(n)) % 26]

def decrypt_room(room):
    return ''.join([decrypt_letter(l, room[1]) for l in room[0]]), int(room[1])

decrypted_rooms = [decrypt_room(room) for room in rooms]

msg, sid = [(m, i) for m, i in decrypted_rooms if 'north' in m][0]

print(f"B ::: Secret ID of North Pole Storage Room = {sid}")
