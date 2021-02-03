
import numpy as np


f = open('day22_input.txt')
text = f.readlines()
f.close()


nodes = {}
for line in text[2:]:
    line = line.strip()
    line = line.split()
    size = int(line[1][:-1])
    used = int(line[2][:-1])
    avail = int(line[3][:-1])
    use = int(line[4][:-1])
    node = line[0].split('-')
    node = (int(node[1][1:]), int(node[2][1:]))
    nodes[node] = [used, avail]

grid = np.array([['#' for _ in range(37)] for __ in range(27)])
for A in nodes.keys():
    for B in nodes.keys():
        if A != B:
            if nodes[A][0] == 0:
                grid[A[1], A[0]] = '_'
                for C in nodes.keys():
                    if A != C:
                        if nodes[A][1] >= nodes[C][0]:
                            grid[C[1], C[0]] = '.'

row = np.where(grid == '_')[0][0]
col = np.where(grid == '_')[1][0]
moveleft = 1 + col - min(np.where(grid == '#')[1])
maxcol = len(grid[0,:]) - 1
print(row + maxcol - col + 2*moveleft + 5*(maxcol - 1))
