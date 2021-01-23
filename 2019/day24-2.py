
from copy import deepcopy
import numpy as np


f = open('day24-1_input.txt')
# f = open('day24-1_debug.txt')
text = f.readlines()
f.close()

minutes = 200
emptygrid = [[['.' for _ in range(7)] for __ in range(7)] for ___ in range(2*minutes+3)]
flatgrid = [['.' for _ in range(7)]]
for line in text:
    line = line.strip()
    line = '.' + line + '.'
    flatgrid.append(list(line))
flatgrid.append(['.' for _ in range(7)])
emptygrid[minutes+1] = flatgrid
grid = np.array(emptygrid)
for _ in range(minutes):
    newgrid = deepcopy(grid)
    for lev in range(1, 2*minutes + 1):
        for row in range(1,6):
            for col in range(1,6):
                if row == 3 and col == 3: continue
                adjacent = 0
                if row == 1:
                    if grid[lev-1, 2, 3] == '#': adjacent += 1
                    if grid[lev, row+1, col] == '#': adjacent += 1
                    if col == 1:
                        if grid[lev-1, 3, 2] == '#': adjacent += 1
                        if grid[lev, row, col+1] == '#': adjacent += 1
                    elif col == 5:
                        if grid[lev-1, 3, 4] == '#': adjacent += 1
                        if grid[lev, row, col-1] == '#': adjacent += 1
                    else:
                        if grid[lev, row, col-1] == '#': adjacent += 1
                        if grid[lev, row, col+1] == '#': adjacent += 1
                elif row == 5:
                    if grid[lev-1, 4, 3] == '#': adjacent += 1
                    if grid[lev, row-1, col] == '#': adjacent += 1
                    if col == 1:
                        if grid[lev-1, 3, 2] == '#': adjacent += 1
                        if grid[lev, row, col+1] == '#': adjacent += 1
                    elif col == 5:
                        if grid[lev-1, 3, 4] == '#': adjacent += 1
                        if grid[lev, row, col-1] == '#': adjacent += 1
                    else:
                        if grid[lev, row, col-1] == '#': adjacent += 1
                        if grid[lev, row, col+1] == '#': adjacent += 1
                elif col == 1:
                    if grid[lev, row+1, col] == '#': adjacent += 1
                    if grid[lev, row-1, col] == '#': adjacent += 1
                    if grid[lev, row, col+1] == '#': adjacent += 1
                    if grid[lev-1, 3, 2] == '#': adjacent += 1
                elif col == 5:
                    if grid[lev, row+1, col] == '#': adjacent += 1
                    if grid[lev, row-1, col] == '#': adjacent += 1
                    if grid[lev, row, col-1] == '#': adjacent += 1
                    if grid[lev-1, 3, 4] == '#': adjacent += 1
                elif row == 2 and col == 3:
                    if grid[lev, row-1, col] == '#': adjacent += 1
                    if grid[lev, row, col-1] == '#': adjacent += 1
                    if grid[lev, row, col+1] == '#': adjacent += 1
                    adjacent += len(np.where(grid[lev+1,1,:] == '#')[0])
                elif row == 4 and col == 3:
                    if grid[lev, row+1, col] == '#': adjacent += 1
                    if grid[lev, row, col-1] == '#': adjacent += 1
                    if grid[lev, row, col+1] == '#': adjacent += 1
                    adjacent += len(np.where(grid[lev+1,5,:] == '#')[0])
                elif row == 3 and col == 2:
                    if grid[lev, row-1, col] == '#': adjacent += 1
                    if grid[lev, row, col-1] == '#': adjacent += 1
                    if grid[lev, row+1, col] == '#': adjacent += 1
                    adjacent += len(np.where(grid[lev+1,:,1] == '#')[0])
                elif row == 3 and col == 4:
                    if grid[lev, row-1, col] == '#': adjacent += 1
                    if grid[lev, row, col+1] == '#': adjacent += 1
                    if grid[lev, row+1, col] == '#': adjacent += 1
                    adjacent += len(np.where(grid[lev+1,:,5] == '#')[0])
                else:
                    if grid[lev, row+1, col] == '#': adjacent += 1
                    if grid[lev, row-1, col] == '#': adjacent += 1
                    if grid[lev, row, col-1] == '#': adjacent += 1
                    if grid[lev, row, col+1] == '#': adjacent += 1

                if adjacent == 1: newgrid[lev, row, col] = '#'
                elif adjacent == 2 and grid[lev, row, col] == '.': newgrid[lev, row, col] = '#'    
                else: newgrid[lev, row, col] = '.'
    grid = newgrid

print(len(np.where(grid == '#')[0]))
