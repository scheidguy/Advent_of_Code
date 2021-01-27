
import numpy as np


f = open('day6_input.txt')
text = f.readlines()
f.close()

display = -1 * np.ones((10**3, 10**3))
for line in text:
    line = line.strip()
    if 'turn on' in line:
        coords = line[8:].split(' through ')
        coords1 = list(map(int, coords[0].split(',')))
        coords2 = list(map(int, coords[1].split(',')))
        display[coords1[0]:coords2[0]+1, coords1[1]:coords2[1]+1] = 1
    if 'turn off' in line:
        coords = line[9:].split(' through ')
        coords1 = list(map(int, coords[0].split(',')))
        coords2 = list(map(int, coords[1].split(',')))
        display[coords1[0]:coords2[0]+1, coords1[1]:coords2[1]+1] = -1
    if 'toggle' in line:
        coords = line[7:].split(' through ')
        coords1 = list(map(int, coords[0].split(',')))
        coords2 = list(map(int, coords[1].split(',')))
        display[coords1[0]:coords2[0]+1, coords1[1]:coords2[1]+1] *= -1
print(len(np.where(display > 0)[0]))
