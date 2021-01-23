
from copy import deepcopy
import numpy as np


f = open('day24-1_input.txt')
# f = open('day24-1_debug.txt')
text = f.readlines()
f.close()

grid = [['.' for _ in range(7)]]
for line in text:
    line = line.strip()
    line = '.' + line + '.'
    grid.append(list(line))
grid.append(['.' for _ in range(7)])

grid = np.array(grid)
SEEN = []
state = ''
for i in range(1,6): state += ''.join(map(str,grid[i][1:-1]))
if state not in SEEN: SEEN.append(state)

while True:
    newgrid = deepcopy(grid)
    for row in range(1,6):
        for col in range(1,6):
            adjacent = 0
            if grid[row-1, col] == '#': adjacent += 1
            if grid[row+1, col] == '#': adjacent += 1
            if grid[row, col-1] == '#': adjacent += 1
            if grid[row, col+1] == '#': adjacent += 1
            if adjacent == 1: newgrid[row, col] = '#'
            elif adjacent == 2 and grid[row, col] == '.': newgrid[row, col] = '#'    
            else: newgrid[row, col] = '.'
    grid = newgrid
    state = ''
    for i in range(1,6): state += ''.join(map(str,grid[i][1:-1]))
    if state not in SEEN: SEEN.append(state)
    else: break

exp = 0
biodiversity = 0
for row in range(1,6):
    for col in range(1,6):
        if grid[row,col] == '#': biodiversity += 2 ** exp
        exp += 1
print(biodiversity)
