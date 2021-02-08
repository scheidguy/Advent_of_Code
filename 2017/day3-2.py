
import numpy as np


def sumneighbors(spiral, row, col):
    thesum = 0
    for aug1 in range(-1, 2, 1):
        for aug2 in range(-1, 2, 1):
            thesum += spiral[row + aug1, col + aug2]
    return thesum

start = 289326
spiral = np.zeros((11, 11), dtype=int)
spiral[5, 5] = 1
layer = 0
row = 5
col = 5
val = 1
foundit = False
while not foundit:
    layer += 1
    col += 1
    for r in range(row, row - 2*layer, -1):
        val = sumneighbors(spiral, r, col)
        if val > start: foundit = True;break
        spiral[r, col] = val
    if foundit: break
    row = r
    col -= 1
    for c in range(col, col - 2*layer, -1):
        val = sumneighbors(spiral, row, c)
        if val > start: foundit = True;break
        spiral[row, c] = val
    if foundit: break
    col = c
    row += 1
    for r in range(row, row + 2*layer):
        val = sumneighbors(spiral, r, col)
        if val > start: foundit = True;break
        spiral[r, col] = val
    if foundit: break
    row = r
    col += 1
    for c in range(col, col + 2*layer):
        val = sumneighbors(spiral, row, c)
        if val > start: foundit = True;break
        spiral[row, c] = val
    col = c

print(val)
