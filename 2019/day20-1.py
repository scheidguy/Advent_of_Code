
# from random import random
import numpy as np
# import math
from copy import deepcopy
# import time


def solve_maze(maze, r, c, destination):
    maze[r, c] = '0'
    steps = 0
    while True:
        rows = np.where(maze == str(steps))[0]
        cols = np.where(maze == str(steps))[1]
        steps += 1
        for i in range(len(rows)):
            r = rows[i]
            c = cols[i]
            down = maze[r+1, c]
            up = maze[r-1, c]
            right = maze[r, c+1]
            left = maze[r, c-1]
            if down == '.': maze[r+1, c] = str(steps)
            if up == '.': maze[r-1, c] = str(steps)
            if right == '.': maze[r, c+1] = str(steps)
            if left == '.': maze[r, c-1] = str(steps)
            if len(down) == 2 and down.isalpha():
                if down == destination: return steps
                maze[r+1, c] = str(steps)
                warp = np.where(maze == down)
                maze[warp[0][0], warp[1][0]] = str(steps + 1)
            if len(up) == 2 and up.isalpha():
                if up == destination: return steps
                maze[r-1, c] = str(steps)
                warp = np.where(maze == up)
                maze[warp[0][0], warp[1][0]] = str(steps + 1)
            if len(right) == 2 and right.isalpha():
                if right == destination: return steps
                maze[r, c+1] = str(steps)
                warp = np.where(maze == right)
                maze[warp[0][0], warp[1][0]] = str(steps + 1)
            if len(left) == 2 and left.isalpha():
                if left == destination: return steps
                maze[r, c-1] = str(steps)
                warp = np.where(maze == left)
                maze[warp[0][0], warp[1][0]] = str(steps + 1)
            


f = open('day20-1_input.txt')
# f = open('day20-1_debug1.txt')
# f = open('day20-1_debug2.txt')
text = f.readlines()
f.close()

m = np.array([list(line.strip('\n')) for line in text], dtype=object)
m = np.insert(m, 0, [' ' for _ in range(len(m[:, 0]))], axis=1)
m = np.append(m, [[' '] for _ in range(len(m[:, 0]))], axis=1)
m = np.insert(m, 0, [' ' for _ in range(len(m[0, :]))], axis=0)
m = np.append(m, [[' ' for _ in range(len(m[0, :]))]], axis=0)
maze = deepcopy(m)
for row in range(len(maze[:, 0])):
    for col in range(len(maze[0, :])):
        if m[row, col].isalpha():
            warp = m[row, col]
            if m[row-1, col].isalpha():
                if m[row-2, col] == '.':
                    maze[row-2, col] = m[row-1, col] + warp
                if m[row+1, col] == '.':
                    maze[row+1, col] = m[row-1, col] + warp
            if m[row, col-1].isalpha():
                if m[row, col-2] == '.':
                    maze[row, col-2] = m[row, col-1] + warp
                if m[row, col+1] == '.':
                    maze[row, col+1] = m[row, col-1] + warp

start = 'AA'
destination = 'ZZ'
row = np.where(maze == start)[0][0]
col = np.where(maze == start)[1][0]
steps = solve_maze(maze, row, col, destination)

print(steps)


