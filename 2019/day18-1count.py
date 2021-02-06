
import numpy as np
from copy import deepcopy
from time import time


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


def get_accessible(grid, gridmap, keys, doors):
    access = ''
    mazemap = deepcopy(gridmap)
    prev = 10**9
    while len(np.where(mazemap == 1)[0]) != prev:
        inds = np.where(mazemap == 1)
        rows = inds[0]
        cols = inds[1]
        prev = len(rows)
        for i in range(len(rows)):
            r = rows[i]
            c = cols[i]
            if (r, c) in keys.values():
                if whatkey[(r, c)] not in access:
                    access += whatkey[(r, c)]
                continue
            down = mazemap[r+1, c]
            up = mazemap[r-1, c]
            right = mazemap[r, c+1]
            left = mazemap[r, c-1]
            if mazemap[r+1, c] == 0 and grid[r+1, c] == -1:
                mazemap[r+1, c] = 1
            if mazemap[r-1, c] == 0 and grid[r-1, c] == -1:
                mazemap[r-1, c] = 1
            if mazemap[r, c+1] == 0 and grid[r, c+1] == -1:
                mazemap[r, c+1] = 1
            if mazemap[r, c-1] == 0 and grid[r, c-1] == -1:
                mazemap[r, c-1] = 1
    access = list(access)
    access.sort()
    access = ''.join(access)
    return access, mazemap
    

def walkpath(access, keys, doors, prevkey, key2key, dependencies, found):
    if set(access) == set('bfagcedh'):
        access = 'a'
    if set(access) == set('gbfdhce'):
        access = 'f'
    if set(access) == set('bcegdh'):
        access = 'b'
    if set(access) == set('jcegdh'):
        access = 'j'
    # if set(access) == set('cegdh'):
    #     access = 'g'
    # if set(access) == set('ndhce'):
    #     access = 'n'
    # if set(access) == set('dhce'):
    #     access = 'h'
    # if set(access) == set('dce'):
    #     access = 'd'
    # if set(access) == set('lceo'):
    #     access = 'l'
    s = 0
    for key in access:
        newaccess = access.replace(key, '')
        newfound = found + key
        for k in dependencies.keys():
            if k not in newfound and k not in newaccess:
                if set(newfound).issuperset(set(dependencies[k])):
                    newaccess += k
        if len(newaccess) > 0:
            s += len(newaccess) -1 
            s += walkpath(newaccess, keys, doors, key, key2key, dependencies, newfound)
    return s


tic = time()
# f = open('day18-1_debug1.txt')
# f = open('day18-1_debug2.txt')
# f = open('day18-1_debug3.txt')
# f = open('day18-1_debug4.txt')
# f = open('day18-1_debug5.txt')
f = open('day18-1_input.txt')
text = f.readlines()
f.close()

grid = []
doors = {}
keys = {}
whatkey = {}
for line in text:
    line = line.strip()
    row = []
    for letter in line:
        row.append(-1)
        if letter == '#':
            row[-1] = 10**4
        elif letter == '@':
            startrow = len(grid)
            startcol = line.index(letter)
        elif letter.isupper():
            doors[letter] = (len(grid), line.index(letter))
            whatkey[(len(grid), line.index(letter))] = letter
        elif letter.islower():
            keys[letter] = (len(grid), line.index(letter))
            whatkey[(len(grid), line.index(letter))] = letter
    grid.append(row)
    
grid = np.array(grid, dtype=int)
gridmap = deepcopy(grid)
gridmap[gridmap == -1] = 0
gridmap[startrow, startcol] = 1

# make a dict with minsteps to each other key from current key
key2key = {}
for key1 in keys.keys():
    key2key['0' + key1] = solvemaze(startrow, startcol, keys[key1][0], keys[key1][1], deepcopy(grid))
    for key2 in keys.keys():
        if key1 == key2 or key1+key2 in key2key.keys():
            continue
        key2key[key1 + key2] = solvemaze(keys[key1][0], keys[key1][1], keys[key2][0], keys[key2][1], deepcopy(grid))
        key2key[key2 + key1] = key2key[key1 + key2]

# figure out dependencies to get each key
maze = deepcopy(grid)
maze[startrow, startcol] = 0
steps = 0
inds = np.where(maze == steps)
dependencies = {}
while len(inds[0]) > 0:
    inds = np.where(maze == steps)
    steps += 1
    rows = inds[0]
    cols = inds[1]
    for i in range(len(rows)):
        row = rows[i]
        col = cols[i]
        if (row, col) in keys.values():
            r = row
            c = col
            key = whatkey[(r, c)]
            needed = ''
            backtrack = steps - 1
            while backtrack != 0:
                backtrack -= 1
                if maze[r + 1, c] == backtrack:
                    r += 1
                elif maze[r - 1, c] == backtrack:
                    r -= 1
                elif maze[r, c + 1] == backtrack:
                    c += 1
                elif maze[r, c - 1] == backtrack:
                    c -= 1
                if (r, c) in whatkey.keys():
                    needed += whatkey[(r, c)].lower()
            dependencies[key] = needed
        if maze[row + 1, col] == -1:
            maze[row + 1, col] = steps
        if maze[row - 1, col] == -1:
            maze[row - 1, col] = steps
        if maze[row, col + 1] == -1:
            maze[row, col + 1] = steps
        if maze[row, col - 1] == -1:
            maze[row, col - 1] = steps

# lock the doors
for door in doors.values():
    grid[door[0], door[1]] = 10**4

access, gridmap = get_accessible(grid, gridmap, keys, doors)

found = ''
steps = 1 + walkpath(access, keys, doors, '0', key2key, dependencies, found)

print(steps)
print(f'TIME ELAPSED: {round(time()-tic)} seconds')
