
import numpy as np
import copy


f = open('day17-1_input.txt')
# f = open('day17-1_debug.txt')
text = f.readlines()
f.close()

numrows = len(text)
initial = np.zeros((numrows,numrows))
row = -1
for line in text:
    row += 1
    line = line.strip()
    col = -1
    for l in line:
        col += 1
        if l == '#': initial[row,col] = 1

ROWS = numrows+2*6+2  # +2 adds perimeter
COLS = ROWS  # because square inputs
LAYERS = 1 + 2*6 + 2  # 1 is initial layer, +2 adds perimeter

state = np.zeros((ROWS, ROWS, LAYERS))
state[7:7+numrows, 7:7+numrows, 7] = initial

# if # and 2 or 3 neighbors are #, still #, otherwise become .
# if . and 3 neighbors are #, become #
prevstate = copy.deepcopy(state)
for cycle in range(6):
    for x in range(1, ROWS - 1):
        for y in range(1, ROWS - 1):
            for z in range(1, LAYERS - 1):
                cube = prevstate[x,y,z]
                if cube == 1:
                    # -1 to not include self
                    neighbors = prevstate[x-1:x+2, y-1:y+2, z-1:z+2].sum() - 1
                    if neighbors < 2 or neighbors > 3: state[x,y,z] = 0
                else:
                    neighbors = prevstate[x-1:x+2, y-1:y+2, z-1:z+2].sum()
                    if neighbors == 3: state[x,y,z] = 1
    prevstate = copy.deepcopy(state)


print(int(state.sum()))