
# import numpy as np


f = open('day14-1_input.txt')
# f = open('day14-1_debug.txt')
text = f.readlines()
f.close()


def howmuch(output, chems, amounts, inventory, used):
    for inp in chems[output]:
        inp = inp.strip().split(' ')
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
                howmuch(inp, chems, amounts, inventory, used)


chems = {}
amounts = {}
inventory = {}
used = {}
ore = {}
for line in text:
    left = (line.strip().split(' => ')[0]).split(',')
    right = (line.strip().split(' => ')[1]).split(' ')
    output = right[1]
    chems[output] = left
    amounts[output] = int(right[0])
    inventory[output] = 0
    used[output] = 0
    if left[0][-3:] == 'ORE': ore[output] = int(left[0].strip().split(' ')[0])

howmuch('FUEL', chems, amounts, inventory, used)

orecount = 0
for key in ore.keys():
    amt = 0
    quota = inventory[key]
    while amt < quota:
        amt += amounts[key]
        orecount += ore[key]

print(orecount)
