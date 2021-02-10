
import numpy as np


f = open('day21_input.txt')
text = f.readlines()
f.close()

enhancements = {}
for line in text:
    line = line.strip().split(' => ')
    result = [list(row) for row in line[1].split('/')]
    result = np.array(result)
    line[0] = line[0].split('/')
    grid = np.array([list(row) for row in line[0]])
    for flips in range(2):
        for rotations in range(4):
            orientation = ''
            for row in range(len(grid[0, :])):
                orientation += ''.join(grid[row, :])
            enhancements[orientation] = result
            grid = np.rot90(grid)
        grid = np.fliplr(grid)

image = np.array([list('.#.'), list('..#'), list('###')])
for iterations in range(5):
    size = len(image[0, :])
    if size % 2 == 0:
        newsize = (size // 2) * 3
        enhanced = np.array([['' for _ in range(newsize)] for __ in range(newsize)])
        for rowstart in range(size // 2):
            for colstart in range(size // 2):
                panel = ''.join(image[2*rowstart, 2*colstart:2*colstart+2])
                panel += ''.join(image[2*rowstart+1, 2*colstart:2*colstart+2])
                enhanced[3*rowstart:3*rowstart+3, 3*colstart:3*colstart+3] = enhancements[panel]
    else:
        newsize = (size // 3) * 4
        enhanced = np.array([['' for _ in range(newsize)] for __ in range(newsize)])
        for rowstart in range(size // 3):
            for colstart in range(size // 3):
                panel = ''.join(image[3*rowstart, 3*colstart:3*colstart+3])
                panel += ''.join(image[3*rowstart+1, 3*colstart:3*colstart+3])
                panel += ''.join(image[3*rowstart+2, 3*colstart:3*colstart+3])
                enhanced[4*rowstart:4*rowstart+4, 4*colstart:4*colstart+4] = enhancements[panel]
    image = enhanced

print(len(np.where(image == '#')[0]))
