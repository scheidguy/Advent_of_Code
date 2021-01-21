
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


def get_shortest(m, R, C, keys):
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
    # if keys == 'dhce':
    #     keys = 'h'
    # if keys == 'dce':
    #     keys = 'd'
    # if keys == 'lceo':
    #     keys = 'l'
    for key in keys:
        s = 0
        maz = deepcopy(m)
        row = R
        col = C
        keymaze = deepcopy(maz)
        keymaze[row, col] = '0'
        keysteps = 0
        while len(np.where(keymaze == key)[0]) > 0:
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
                if up == '.': keymaze[r-1, c] = str(keysteps)
                if right == '.': keymaze[r, c+1] = str(keysteps)
                if left == '.': keymaze[r, c-1] = str(keysteps)
                if key in [up, down, left, right]:
                    s += keysteps
                    row = np.where(keymaze == key)[0][0]
                    col = np.where(keymaze == key)[1][0]
                    keymaze[row, col] = '.'
                    maz[row, col] = '.'
                    while len(np.where(keymaze == key.upper())[0]) != 0:
                        doorrow = np.where(keymaze == key.upper())[0][0]
                        doorcol = np.where(keymaze == key.upper())[1][0]
                        keymaze[doorrow, doorcol] = '.'
                        maz[doorrow, doorcol] = '.'
                    newkeys = get_accessible(maz, row, col)
                    if len(newkeys) > 0:
                        s += get_shortest(maz, row, col, newkeys)
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
row = np.where(maze == '@')[0][0]
col = np.where(maze == '@')[1][0]
maze[row, col] = '.'
steps = 0
keys = get_accessible(maze, row, col)
steps = get_shortest(maze, row, col, keys)

print(steps)
toc = time.time()
print(f'TIME ELAPSED: {toc-tic} seconds')
