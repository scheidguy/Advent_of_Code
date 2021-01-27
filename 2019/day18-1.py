
import time
import numpy as np
from string import ascii_lowercase as asci
from copy import deepcopy


def get_accessible(m, r, c):
    access = ''
    keymaze = deepcopy(m)
    keymaze[r, c] = '0'
    keysteps = 0
    prev = 10**9
    while len(np.where(keymaze == '.')[0]) != prev:
        prev = len(np.where(keymaze == '.')[0])
        rows = np.where(keymaze == str(keysteps))[0]
        cols = np.where(keymaze == str(keysteps))[1]
        keysteps += 1
        for i in range(len(rows)):
            r = rows[i]
            c = cols[i]
            down = keymaze[r+1, c]
            up = keymaze[r-1, c]
            right = keymaze[r, c+1]
            left = keymaze[r, c-1]
            if down == '.': keymaze[r+1, c] = str(keysteps)
            elif down in asci: access += down;keymaze[r+1, c] = '!'
            if up == '.': keymaze[r-1, c] = str(keysteps)
            elif up in asci: access += up;keymaze[r-1, c] = '!'
            if right == '.': keymaze[r, c+1] = str(keysteps)
            elif right in asci: access += right;keymaze[r, c+1] = '!'
            if left == '.': keymaze[r, c-1] = str(keysteps)
            elif left in asci: access += left;keymaze[r, c-1] = '!'
    return access


def get_shortest(m, R, C, keys, bestpaths):
    shortest = 10**9
    if keys == 'bfagcedh':
        keys = 'a'
    if keys == 'gbfdhce':
        keys = 'f'
    if keys == 'bcegdh':
        keys = 'b'
    if keys == 'jcegdh':
        keys = 'j'
    if keys == 'cegdh':
        keys = 'g'
    if keys == 'ndhce':
        keys = 'n'
    if keys == 'dhce':
        keys = 'h'
    if keys == 'dce':
        keys = 'd'
    if keys == 'lceo':
        keys = 'l'
    for key in keys:
        s = 0
        maz = deepcopy(m)
        keymaze = deepcopy(maz)
        row = np.where(m == key)[0][0]
        col = np.where(m == key)[1][0]
        keysteps = bestpaths[str(R) + ',' + str(C)][row, col]
        s += keysteps
        keymaze[row, col] = '.'
        maz[row, col] = '.'
        while len(np.where(keymaze == key.upper())[0]) != 0:
            doorrow = np.where(keymaze == key.upper())[0][0]
            doorcol = np.where(keymaze == key.upper())[1][0]
            keymaze[doorrow, doorcol] = '.'
            maz[doorrow, doorcol] = '.'
        newkeys = get_accessible(maz, row, col)
        if len(newkeys) > 0:
            s += get_shortest(maz, row, col, newkeys, bestpaths)
        if s < shortest: shortest = s
    return shortest


tic = time.time()
# f = open('day18-1_input.txt')
# f = open('day18-1_debug1.txt')
# f = open('day18-1_debug2.txt')
# f = open('day18-1_debug3.txt')
f = open('day18-1_debug4.txt')
# f = open('day18-1_debug5.txt')
text = f.readlines()
f.close()

maze = np.array([list(line.strip()) for line in text], dtype=object)
initialrow = np.where(maze == '@')[0][0]
initialcol = np.where(maze == '@')[1][0]
maze[initialrow, initialcol] = '.'
template = -1 * np.ones((len(maze[:,0]), len(maze[0,:])), dtype=int)
rows = np.where(maze == '#')[0]
cols = np.where(maze == '#')[1]
for i in range(len(rows)): template[rows[i], cols[i]] = -9
bestpaths = {}
for row in range(len(maze[:, 0])):
    for col in range(len(maze[0, :])):
        if maze[row, col] == '#': continue
        steps = 0
        bestmaze = deepcopy(template)
        bestmaze[row, col] = 0
        while len(np.where(bestmaze == -1)[0]) > 0:
            rows = np.where(bestmaze == steps)[0]
            cols = np.where(bestmaze == steps)[1]
            steps += 1
            for i in range(len(rows)):
                r = rows[i]
                c = cols[i]
                down = bestmaze[r+1, c]
                up = bestmaze[r-1, c]
                right = bestmaze[r, c+1]
                left = bestmaze[r, c-1]
                if down == -1: bestmaze[r+1, c] = steps
                if up == -1: bestmaze[r-1, c] = steps
                if right == -1: bestmaze[r, c+1] = steps
                if left == -1: bestmaze[r, c-1] = steps
        bestpaths[str(row) + ',' + str(col)] = bestmaze

keys = get_accessible(maze, initialrow, initialcol)
steps = get_shortest(maze, initialrow, initialcol, keys, bestpaths)

print(steps)
toc = time.time()
print(f'TIME ELAPSED: {toc-tic} seconds')
