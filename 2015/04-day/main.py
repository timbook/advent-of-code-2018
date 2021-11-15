from hashlib import md5

input_ = 'ckczppom'

n = 1
while True:
    value = input_ + str(n)
    res = md5(value.encode()).hexdigest()
    if res[:5] == '00000':
        break
    n += 1

print('A :::')
print(f'The smallest int yielding 5 zeros = {n}')
print()

n = 1
while True:
    value = input_ + str(n)
    res = md5(value.encode()).hexdigest()
    if res[:6] == '000000':
        break
    n += 1

print('B :::')
print(f'The smallest int yielding 6 zeros = {n}')
