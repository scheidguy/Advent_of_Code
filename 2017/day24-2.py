
from copy import deepcopy
import numpy as np


def buildbridge(components, port, length):
    length += 1
    fits = np.where(components == port)[0]
    strongest = 0
    for ind in fits:
        c = deepcopy(components)
        score = port
        if ind % 2 == 0:
            newport = c[ind+1]
            c[ind+1] = -1
        else:
            newport = c[ind-1]
            c[ind-1] = -1
        c[ind] = -1
        score += newport
        if newport in c:
            score += buildbridge(c, newport, length)
        if score > strongest:
            strongest = score
        if length > 39:
            print(sum(c))
    return strongest


f = open('day24_input.txt')
text = f.readlines()
f.close()

components = []
for line in text:
    line = line.strip().split('/')
    components.append(int(line[0]))
    components.append(int(line[1]))

components = np.array(components)
print(buildbridge(components, 0, 0))
