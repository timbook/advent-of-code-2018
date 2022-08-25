from hashlib import md5

key = 'reyedfim'

chars = []
n = 0
while len(chars) < 8:
    hash_in = (key + str(n)).encode()
    res = md5(hash_in).hexdigest()
    if res[:5] == '00000':
        chars.append(res[5])
    n += 1

print(f"A ::: Password = {''.join(chars)}")

class Code:
    def __init__(self):
        self.password = {}
        self.all_finds = {}

    def insert_key(self, value, pos):
        self.all_finds[pos] = value
        if pos in '01234567' and int(pos) not in self.password:
            self.password[int(pos)] = value

    def is_done(self):
        return all(n in self.password for n in range(8))

    def get_res(self):
        return ''.join([self.password.get(i, 'X') for i in range(8)])

code = Code()

n = 0
while not code.is_done():
    hash_in = (key + str(n)).encode()
    res = md5(hash_in).hexdigest()
    if res[:5] == '00000':
        code.insert_key(res[6], res[5])
    n += 1

print(f"B ::: Password = {code.get_res()}")
