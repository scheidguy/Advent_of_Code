
import numpy as np


f = open('day19_input.txt')
text = f.readlines()
f.close()

route = []
for line in text:
    line = line.strip('\n')
    route.append(list(line))

route = np.array(route)
direction = 'south'
row = 0
col = np.where(route[0, :] == '|')[0][0]
path = ''
nextone = route[row, col]
steps = 0
while nextone != ' ':
    steps += 1
    if direction == 'south':
        row += 1
        nextone = route[row, col]
        if nextone.isalpha():
            path += nextone
        if nextone == '+':
            if col > 0:
                if route[row, col - 1] == '-':
                    direction = 'west'
            if col + 1 < len(route[0, :]):
                if route[row, col + 1] == '-':
                    direction = 'east'
    elif direction == 'north':
        row -= 1
        nextone = route[row, col]
        if nextone.isalpha():
            path += nextone
        if nextone == '+':
            if col > 0:
                if route[row, col - 1] == '-':
                    direction = 'west'
            if col + 1 < len(route[0, :]):
                if route[row, col + 1] == '-':
                    direction = 'east'
    elif direction == 'east':
        col += 1
        nextone = route[row, col]
        if nextone.isalpha():
            path += nextone
        if nextone == '+':
            if row > 0:
                if route[row - 1, col] == '|':
                    direction = 'north'
            if row + 1 < len(route[:, 0]):
                if route[row + 1, col] == '|':
                    direction = 'south'
    elif direction == 'west':
        col -= 1
        nextone = route[row, col]
        if nextone.isalpha():
            path += nextone
        if nextone == '+':
            if row > 0:
                if route[row - 1, col] == '|':
                    direction = 'north'
            if row + 1 < len(route[:, 0]):
                if route[row + 1, col] == '|':
                    direction = 'south'

print(steps)
