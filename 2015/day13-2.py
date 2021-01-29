
from itertools import permutations
import numpy as np


f = open('day13_input.txt')
text = f.readlines()
f.close()

people = ['Alice','Bob','Carol','David','Eric','Frank','George','Mallory']
scores = np.zeros((len(people)+1, len(people)+1))
perms = permutations(list(range(len(people)+1)))

for line in text:
    line = line.strip()
    line = line.strip('.')
    line = line.split(' ')
    row = people.index(line[0])
    col = people.index(line[-1])
    pos = '+'
    if line[2] == 'lose': pos = '-'
    num = int(pos + line[3])
    scores[row, col] = num

happiest = 0
for perm in perms:
    happiness = 0
    for i in range(len(perm)):
        if i == 0:
            happiness += scores[perm[i], perm[-1]]
            happiness += scores[perm[i], perm[i+1]]
        elif i == len(perm) - 1:
            happiness += scores[perm[i], perm[i-1]]
            happiness += scores[perm[i], perm[0]]
        else:
            happiness += scores[perm[i], perm[i-1]]
            happiness += scores[perm[i], perm[i+1]]
    if happiness > happiest:
        happiest = happiness

print(happiest)
