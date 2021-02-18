
import numpy as np


serialnum = 8444
grid = np.ones((301, 301), dtype=int)
for x in range(1, grid.shape[1]):
    for y in range(1, grid.shape[0]):
        rackID = x + 10
        power = rackID * y + serialnum
        power *= rackID
        power = str(power)
        if len(power) > 2:
            power = int(power[-3]) - 5
        else:
            power = -5
        grid[y, x] = power

largest = 0
for dim in range(1, 301):
    if dim % 10 == 0: print(dim)
    for x in range(dim, grid.shape[1]):
        for y in range(dim, grid.shape[0]):
            square3 = np.sum(grid[y-dim+1:y+1, x-dim+1:x+1])
            if square3 > largest:
                largest = square3
                topleft = (x-dim+1, y-dim+1, dim)

print(','.join(map(str, topleft)))       
