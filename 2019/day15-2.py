
# from random import random
import numpy as np
# import math


f = open('day15-1_map.txt')
# f = open('day15-1_debug.txt')
text = f.readlines()
f.close()

grid = [list(map(int, line.strip().split(' '))) for line in text]
grid = np.array(grid)


time = 0
while len(np.where(grid == 1)[0]):
    time += 1
    coords = np.where(grid == 1)
    adjacent = []
    for i in range(len(coords[0])):
        row = coords[0][i]
        col = coords[1][i]
        if grid[row+1, col] == 2: adjacent.append((row, col))
        elif grid[row-1, col] == 2: adjacent.append((row, col))
        elif grid[row, col+1] == 2: adjacent.append((row, col))
        elif grid[row, col-1] == 2: adjacent.append((row, col))
    for rc in adjacent: grid[rc[0], rc[1]] = 2

print(time)
