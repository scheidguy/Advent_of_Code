
import numpy as np


f = open('day22_input.txt')
text = f.readlines()
f.close()

size = 10**3
grid = np.array([['.' for _ in range(size)] for __ in range(size)])
row = size // 2 - 1
for line in text:
    row += 1
    line = line.strip()
    grid[row, size//2 : size//2 + 25] = list(line)

row = size // 2 + 12
col = size // 2 + 12
direction = 'north'
infected = 0
for burst in range(10000):
    if grid[row, col] == '#':
        grid[row, col] = '.'
        if direction == 'north':
            direction = 'east'
            col += 1
        elif direction == 'east':
            direction = 'south'
            row += 1
        elif direction == 'south':
            direction = 'west'
            col -= 1
        elif direction == 'west':
            direction = 'north'
            row -= 1
    else:
        infected += 1
        grid[row, col] = '#'
        if direction == 'north':
            direction = 'west'
            col -= 1
        elif direction == 'east':
            direction = 'north'
            row -= 1
        elif direction == 'south':
            direction = 'east'
            col += 1
        elif direction == 'west':
            direction = 'south'
            row += 1

print(infected)
