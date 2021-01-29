
import numpy as np
from itertools import permutations


f = open('day9_input.txt')
text = f.readlines()
f.close()

dist = np.zeros((8,8))
perms = permutations(list(range(8)), 8)
row = 0
col = 0
for line in text:
    col += 1
    if col == 8:
        row += 1
        col = row + 1
    line = line.strip().split(' = ')
    d = int(line[1])
    dist[row, col] = d
    dist[col, row] = d

longest = 0
for perm in perms:
    length = 0
    for i in range(len(perm) - 1):
        length += dist[perm[i], perm[i+1]]
    if length > longest: longest = length

print(longest)
