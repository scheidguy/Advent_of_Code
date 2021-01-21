
# from random import random
import numpy as np
# import math
from copy import deepcopy
import time


def solve_maze(maze, l, r, c, destination, w):
    maze[l, r, c] = '0'
    steps = 0
    while True:
        levels = np.where(maze == str(steps))[0]
        rows = np.where(maze == str(steps))[1]
        cols = np.where(maze == str(steps))[2]
        steps += 1
        for i in range(len(rows)):
            l = levels[i]
            r = rows[i]
            c = cols[i]
            if l == len(maze[:, 0, 0]) - 1: continue
            down = maze[l, r+1, c]
            up = maze[l, r-1, c]
            right = maze[l, r, c+1]
            left = maze[l, r, c-1]
            if down == '.': maze[l, r+1, c] = str(steps)
            if up == '.': maze[l, r-1, c] = str(steps)
            if right == '.': maze[l, r, c+1] = str(steps)
            if left == '.': maze[l, r, c-1] = str(steps)
            if len(down) == 2 and down.isalpha():
                if down == destination: return steps
                maze[l, r+1, c] = str(steps)
                curr = set()
                curr.add((r+1, c))
                warp = w[down].difference(curr).pop()
                if r+1 > 5 and r+1 < len(maze[0,:,0])-5 and c > 5 and c < len(maze[0,0,:])-5: l += 1
                else: l -= 1
                maze[l, warp[0], warp[1]] = str(steps + 1)
            if len(up) == 2 and up.isalpha():
                if up == destination: return steps
                maze[l, r-1, c] = str(steps)
                curr = set()
                curr.add((r-1, c))
                warp = w[up].difference(curr).pop()
                if r-1 > 5 and r-1 < len(maze[0,:,0])-5 and c > 5 and c < len(maze[0,0,:])-5: l += 1
                else: l -= 1
                maze[l, warp[0], warp[1]] = str(steps + 1)
            if len(right) == 2 and right.isalpha():
                if right == destination: return steps
                maze[l, r, c+1] = str(steps)
                curr = set()
                curr.add((r, c+1))
                warp = w[right].difference(curr).pop()
                if r > 5 and r < len(maze[0,:,0])-5 and c+1 > 5 and c+1 < len(maze[0,0,:])-5: l += 1
                else: l -= 1
                maze[l, warp[0], warp[1]] = str(steps + 1)
            if len(left) == 2 and left.isalpha():
                if left == destination: return steps
                maze[l, r, c-1] = str(steps)
                curr = set()
                curr.add((r, c-1))
                warp = w[left].difference(curr).pop()
                if r > 5 and r < len(maze[0,:,0])-5 and c-1 > 5 and c-1 < len(maze[0,0,:])-5: l += 1
                else: l -= 1
                maze[l, warp[0], warp[1]] = str(steps + 1)
                

tic = time.time()
f = open('day20-1_input.txt')
# f = open('day20-1_debug1.txt')
# f = open('day20-1_debug2.txt')
# f = open('day20-1_debug3.txt')
text = f.readlines()
f.close()

depth = 30
m = np.array([list(line.strip('\n')) for line in text], dtype=object)
m = np.insert(m, 0, [' ' for _ in range(len(m[:, 0]))], axis=1)
m = np.append(m, [[' '] for _ in range(len(m[:, 0]))], axis=1)
m = np.insert(m, 0, [' ' for _ in range(len(m[0, :]))], axis=0)
m = np.append(m, [[' ' for _ in range(len(m[0, :]))]], axis=0)
maze = deepcopy(m)
warpcoords = {}
for row in range(len(maze[:, 0])):
    for col in range(len(maze[0, :])):
        if m[row, col].isalpha():
            warp = m[row, col]
            if m[row-1, col].isalpha():
                if m[row-2, col] == '.':
                    maze[row-2, col] = m[row-1, col] + warp
                    if m[row-1, col] + warp not in warpcoords.keys():
                        warpcoords[m[row-1, col] + warp] = set()
                    warpcoords[m[row-1, col] + warp].add((row-2, col))
                if m[row+1, col] == '.':
                    maze[row+1, col] = m[row-1, col] + warp
                    if m[row-1, col] + warp not in warpcoords.keys():
                        warpcoords[m[row-1, col] + warp] = set()
                    warpcoords[m[row-1, col] + warp].add((row+1, col))
            if m[row, col-1].isalpha():
                if m[row, col-2] == '.':
                    maze[row, col-2] = m[row, col-1] + warp
                    if m[row, col-1] + warp not in warpcoords.keys():
                        warpcoords[m[row, col-1] + warp] = set()
                    warpcoords[m[row, col-1] + warp].add((row, col-2))
                if m[row, col+1] == '.':
                    maze[row, col+1] = m[row, col-1] + warp
                    if m[row, col-1] + warp not in warpcoords.keys():
                        warpcoords[m[row, col-1] + warp] = set()
                    warpcoords[m[row, col-1] + warp].add((row, col+1))

mazes = np.array([maze for _ in range(depth)])
start = 'AA'
destination = 'ZZ'
level = 0

topmaze = mazes[0,:,:]
topmaze[3, :] = '#'
topmaze[:, 3] = '#'
topmaze[-4, :] = '#'
topmaze[:, -4] = '#'
row = np.where(maze == destination)[0][0]
col = np.where(maze == destination)[1][0]
topmaze[row, col] = 'ZZ'
mazes[1:, row, col] = '#'
row = np.where(maze == start)[0][0]
col = np.where(maze == start)[1][0]
topmaze[row, col] = 'AA'
mazes[1:, row, col] = '#'

steps = solve_maze(mazes, level, row, col, destination, warpcoords)

print(steps)
toc = time.time()
print(f'TIME ELAPSED: {round(toc-tic, 1)} seconds')

