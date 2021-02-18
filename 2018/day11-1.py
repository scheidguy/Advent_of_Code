
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
for x in range(3, grid.shape[1]):
    for y in range(3, grid.shape[0]):
        square3 = np.sum(grid[y-2:y+1, x-2:x+1])
        if square3 > largest:
            largest = square3
            topleft = (x-2, y-2)

print(','.join(map(str, topleft)))    
