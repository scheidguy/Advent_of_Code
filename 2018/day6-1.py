
import numpy as np


f = open('day6_input.txt')
text = f.readlines()
f.close()

coordrows = []
coordcols = []
for line in text:
    line = line.strip().split(', ')
    coordrows.append(int(line[1]))
    coordcols.append(int(line[0]))

manhats = {}
numcoords = len(coordrows)
for c in range(numcoords):
    coordrow = coordrows[c]
    coordcol = coordcols[c]
    grid = 10**4 * np.ones((max(coordrows)+2, max(coordcols)+2), dtype=int)
    grid[coordrow, coordcol] = 0
    steps = 0
    inds = np.where(grid == steps)
    rows = inds[0]
    cols = inds[1]
    while len(rows) > 0:
        steps += 1
        for i in range(len(rows)):
            row = rows[i]
            col = cols[i]
            if row == 0 or row == grid.shape[0] - 1:
                continue
            if col == 0 or col == grid.shape[1] - 1:
                continue
            if grid[row+1, col] > steps:
                grid[row+1, col] = steps
            if grid[row-1, col] > steps:
                grid[row-1, col] = steps
            if grid[row, col+1] > steps:
                grid[row, col+1] = steps
            if grid[row, col-1] > steps:
                grid[row, col-1] = steps
        inds = np.where(grid == steps)
        rows = inds[0]
        cols = inds[1]

    manhats[c] = grid

closest = -1 * np.ones((max(coordrows)+2, max(coordcols)+2), dtype=int)
for row in range(closest.shape[0]):
    for col in range(closest.shape[1]):
        distances = [manhats[key][row, col] for key in manhats.keys()]
        if distances.count(min(distances)) == 1:
            closest[row, col] = distances.index(min(distances))

largest = 0
for coord in manhats.keys():
    inds = np.where(closest == coord)
    rows = inds[0]
    cols = inds[1]
    if 1 in rows or 1 in cols:
        continue
    if grid.shape[0] - 2 in rows or grid.shape[1] - 2 in cols:
        continue
    if len(rows) > largest:
        largest = len(rows)
        largestcoord = coord

print(largest)
print(largestcoord)
