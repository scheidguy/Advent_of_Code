
import numpy as np
from itertools import permutations
from copy import deepcopy


def solvemaze(row, col, endrow, endcol, maze):
    steps = 0
    maze[row, col] = 0
    while maze[endrow, endcol] == -1:
        inds = np.where(maze == steps)
        steps += 1
        rows = inds[0]
        cols = inds[1]
        for i in range(len(rows)):
            if maze[rows[i] + 1, cols[i]] == -1:
                maze[rows[i] + 1, cols[i]] = steps
            if maze[rows[i] - 1, cols[i]] == -1:
                maze[rows[i] - 1, cols[i]] = steps
            if maze[rows[i], cols[i] + 1] == -1:
                maze[rows[i], cols[i] + 1] = steps
            if maze[rows[i], cols[i] - 1] == -1:
                maze[rows[i], cols[i] - 1] = steps
    return steps


f = open('day24_input.txt')
text = f.readlines()
f.close()

grid = []
for line in text:
    line = line.strip()
    row = []
    for letter in line:
        if letter == '#':
            row.append(10**4)
        elif letter == '.':
            row.append(-1)
        else:
            row.append(int(letter))
    grid.append(row)
    
grid = np.array(grid, dtype=int)

findme = []
keys = []
for n in range(10):
    rows = np.where(grid == n)[0]
    cols = np.where(grid == n)[1]
    if n == 0:
        startrow = rows[0]
        startcol = cols[0]
    if len(rows) > 0:
        findme.append((rows[0], cols[0]))
        keys.append(n)
        grid[rows[0], cols[0]] = -1

# make a table with minsteps to each other key from current key (null diag)
key2key = np.zeros((len(keys), len(keys)))
for key1 in keys:
    for key2 in keys:
        if key1 == key2: continue
        k1 = keys.index(key1)
        k2 = keys.index(key2)
        key2key[key1, key2] = solvemaze(findme[k1][0], findme[k1][1], findme[k2][0], findme[k2][1], deepcopy(grid))
for key0 in keys:
    k0 = keys.index(key0)
    key2key[0, key0] = solvemaze(startrow, startcol, findme[k0][0], findme[k0][1], deepcopy(grid))

perms = list(permutations(keys[1:]))
minsteps = 10**9
for perm in perms:
    steps = key2key[0, perm[0]]
    for i in range(1, len(perm)):
        steps += key2key[perm[i-1], perm[i]]
    steps += key2key[0, perm[-1]]
    if steps < minsteps:
        minsteps = steps

print(int(minsteps))
