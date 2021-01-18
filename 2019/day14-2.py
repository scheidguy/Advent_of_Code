
import time


tic = time.time()
f = open('day14-1_input.txt')
# f = open('day14-1_debug.txt')
text = f.readlines()
f.close()


def howmuch(output, chems, amounts, inventory, used, extra):
    for inp in chems[output]:
        needed = int(inp[0])
        inp = inp[1]
        if inp == 'ORE':
            return
        else:
            batch = inventory[inp] - used[inp]
            used[inp] += needed
            while batch < needed:
                batch += amounts[inp]
                inventory[inp] += amounts[inp]
                extra[inp] += amounts[inp]
                howmuch(inp, chems, amounts, inventory, used, extra)


chems = {}
amounts = {}
inventory = {}
used = {}
extra = {}
ore = {}
for line in text:
    left = (line.strip().split(' => ')[0]).split(',')
    right = (line.strip().split(' => ')[1]).split(' ')
    output = right[1]
    chems[output] = [inp.strip().split(' ') for inp in left]
    amounts[output] = int(right[0])
    inventory[output] = 0
    used[output] = 0
    extra[output] = 0
    if left[0][-3:] == 'ORE':
        ore[output] = int(left[0].strip().split(' ')[0])

orecount = 0
fuelcount = 0
# seen = [' '.join(map(str, list(inventory.values())))]
while orecount <= 10**12:
    howmuch('FUEL', chems, amounts, inventory, used, extra)
    for key in ore.keys():
        amt = 0
        quota = extra[key]
        while amt < quota:
            amt += amounts[key]
            orecount += ore[key]
    for key2 in used:
        inventory[key2] -= used[key2]
        used[key2] = 0
        extra[key2] = 0
    fuelcount += 1
    if fuelcount % 10000 == 0: print(f'PROCESSING {fuelcount}')
    # vals = ' '.join(map(str, list(inventory.values())))
    # if vals in seen: break
    # else: seen.append(vals)

# numcycles = 10**12 // orecount
# fuelcount *= numcycles
# orecount *= numcycles
# while orecount <= 10**12:
#     howmuch('FUEL', chems, amounts, inventory, used, extra)
#     for key in ore.keys():
#         amt = 0
#         quota = extra[key]
#         while amt < quota:
#             amt += amounts[key]
#             orecount += ore[key]
#     for key2 in used:
#         inventory[key2] -= used[key2]
#         used[key2] = 0
#         extra[key2] = 0
#     fuelcount += 1

fuelcount -= 1
print(f'RESULT  --->  {fuelcount}')
toc = time.time()
print(f'TIME ELAPSED: {round(toc-tic)} seconds')
