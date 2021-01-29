
import numpy as np


f = open('day18_input.txt')
text = f.readlines()
f.close()

size = 100
lights = np.zeros((size+2, size+2))
row = 1
for line in text:
    line = line.strip()
    for col in range(len(line)):
        if line[col] == '#': lights[row, col+1] = 1
    row += 1

for step in range(100):
    new = np.zeros((size+2, size+2))
    for row in range(1, size+1):
        for col in range(1, size+1):
            neighbors = 0
            if lights[row-1, col-1]: neighbors += 1
            if lights[row+1, col+1]: neighbors += 1
            if lights[row+1, col-1]: neighbors += 1
            if lights[row-1, col+1]: neighbors += 1
            if lights[row, col-1]: neighbors += 1
            if lights[row-1, col]: neighbors += 1
            if lights[row, col+1]: neighbors += 1
            if lights[row+1, col]: neighbors += 1
            
            if neighbors == 3: new[row, col] = 1
            elif lights[row, col] and neighbors == 2: new[row, col] = 1
    lights = new

print(np.sum(lights))
