
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

garden = ['.' for _ in range(100)]
garden.extend(initial)
garden.extend(['.' for _ in range(100)])
for gen in range(20):
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
        thesum += i-100

print(thesum)
