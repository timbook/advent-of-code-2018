from pdb import set_trace
from collections import deque

N = 607331

recipes = [3, 7]
elf_1 = 0
elf_2 = 1

def iterate():
    global elf_1
    global elf_2
    new_recipe = recipes[elf_1] + recipes[elf_2]
    if new_recipe < 10:
        recipes.append(new_recipe)
    else:
        new_str = str(new_recipe)
        recipes.append(int(new_str[0]))
        recipes.append(int(new_str[1]))
    elf_1 = (elf_1 + recipes[elf_1] + 1) % len(recipes)
    elf_2 = (elf_2 + recipes[elf_2] + 1) % len(recipes)


while len(recipes) <= N + 10:
    iterate()

next_10 = ''.join(str(r) for r in recipes[N:(N + 10)])

print("::: PART A")
print(f"The next 10 scores are: {next_10}\n")

#==============================================================================

recipes = [3, 7]
elf_1 = 0
elf_2 = 1

i = 0
str_recipes = ''
while True:
    iterate()
    last_np1 = ''.join(str(r) for r in recipes[-(len(str(N)) + 1):])
    if last_np1[1:] == str(N) or last_np1[:-1] == str(N):
        break
    i += 1

str_recipes = ''.join(str(r) for r in recipes)
print("::: PART B")
print(f"It is done! Answer is {str_recipes.index(str(N))}")
