
from copy import deepcopy


f = open('day12_input.txt')
text = f.readlines()
f.close()

rules = []
for line in text:
    line = line.strip().split()
    if 'initial' in line[0]:
        initial = list(line[-1])
    elif line[-1] == '#':
        rules.append(list(line[0]))

generations = 100
garden = ['.' for _ in range(10)]
garden.extend(initial)
garden.extend(['.' for _ in range(2*generations)])
SEEN = set()
gencycle = []
for gen in range(generations):
    firstind = garden.index('#')
    lastind = len(garden) - garden[::-1].index('#') - 1
    strgarden = ''.join(garden[firstind:lastind+1])
    if strgarden not in SEEN:
        SEEN.add(strgarden)
    else:
        gencycle.append(gen)
        print(firstind)
    newgarden = deepcopy(garden)
    for i in range(2, len(garden) - 2):
        checkit = [garden[j] for j in range(i-2, i+3)]
        if checkit in rules:
            newgarden[i] = '#'
        else:
            newgarden[i] = '.'
    garden = newgarden

thesum = 0
for i in range(len(garden)):
    if garden[i] == '#':
        thesum += i-10

thesum += (50000000000 - 100) * garden.count('#')

print(thesum)
