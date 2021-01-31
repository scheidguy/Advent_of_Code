
import numpy as np


f = open('day8_input.txt')
text = f.readlines()
f.close()

screen = np.zeros((6, 50), dtype=int)
for line in text:
    line = line.strip()
    if 'rect' in line:
        x = line.index('x')
        rows = int(line[x+1:x+3])
        cols = int(line[x-2:x])
        screen[0:rows, 0:cols] = 1
    if 'rotate row' in line:
        equal = line.index('=')
        row = int(line[equal+1:equal+3])
        amount = int(line[-2:])
        screen[row, :] = np.concatenate((screen[row, -amount:], screen[row, 0:-amount]))
    if 'rotate col' in line:
        equal = line.index('=')
        col = int(line[equal+1:equal+3])
        amount = int(line[-2:])
        screen[:, col] = np.concatenate((screen[-amount:, col], screen[0:-amount, col]))

for row in range(6):
    print(''.join(list(map(str, screen[row, :]))))
