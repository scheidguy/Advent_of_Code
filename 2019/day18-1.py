
import time
import numpy as np
import string
from copy import deepcopy


# def find_next_key(k, m, r, c):
#     track = deepcopy(m)
#     substeps = 0
#     while 

tic = time.time()
# f = open('day18-1_input.txt')
f = open('day18-1_debug.txt')
text = f.readlines()
f.close()

alph = string.ascii_lowercase
Alph = string.ascii_uppercase
maze = np.array([list(line.strip()) for line in text], dtype=object)
row = np.where(maze == '@')[0][0]
col = np.where(maze == '@')[1][0]


steps = 0
for key in alph:
    if len(np.where(maze == key)[0]) == 0: break
    keymaze = deepcopy(maze)
    keymaze[row, col] = '0'
    keysteps = 0
    while len(np.where(keymaze == key)[0]) > 0:
        rows = np.where(keymaze == str(keysteps))[0]
        cols = np.where(keymaze == str(keysteps))[1]
        keysteps += 1
        for i in range(len(rows)):
            r = rows[i]
            c = cols[i]
            if keymaze[r+1, c] in alph+'.@': keymaze[r+1, c] = str(keysteps)
            if keymaze[r-1, c] in alph+'.@': keymaze[r-1, c] = str(keysteps)
            if keymaze[r, c+1] in alph+'.@': keymaze[r, c+1] = str(keysteps)
            if keymaze[r, c-1] in alph+'.@': keymaze[r, c-1] = str(keysteps)
    steps += keysteps
    row = np.where(maze == key)[0][0]
    col = np.where(maze == key)[1][0]
    maze[row, col] = '.'
    if len(np.where(maze == key.upper())[0]) != 0:
        doorrow = np.where(maze == key.upper())[0][0]
        doorcol = np.where(maze == key.upper())[1][0]
        maze[doorrow, doorcol] = '.'

print(steps)
