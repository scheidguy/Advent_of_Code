
from random import random
import numpy as np
import math


f = open('day15-1_input.txt')
# f = open('day15-1_debug.txt')
text = f.readlines()
f.close()

program = [int(i) for i in text[0].strip().split(',')]
program.extend([0 for _ in range(10**5)])

grid = np.ones((50, 50)) * -1
grid[:,0] = 0
grid[:,-1] = 0
grid[0,:] = 0
grid[-1,:] = 0
row = col = 50 // 2
pos = 0
rel = 0
inp = 1
moves = 0
while moves < 10**6:
    command = str(program[pos])
    command = '0'*(5-len(command)) + command
    opcode = command[-2:]
    modes = command[0:-2]
    if opcode == '99':
        break

    if modes[2] == '0': first = program[program[pos+1]]
    if modes[2] == '1': first = program[pos+1]
    if modes[2] == '2': first = program[rel + program[pos+1]]
    if opcode in ['01', '02', '05', '06', '07', '08']:
        if modes[1] == '0': second = program[program[pos+2]]
        if modes[1] == '1': second = program[pos+2]
        if modes[1] == '2': second = program[rel + program[pos+2]]
        if opcode in ['01', '02', '07', '08']:
            if modes[0] == '0': third = program[pos+3]
            if modes[0] == '1': third = pos+3
            if modes[0] == '2': third = rel + program[pos+3]
    
    if opcode == '01':
        program[third] = first + second
        pos += 4
    elif opcode == '02':
        program[third] = first * second
        pos += 4
    elif opcode == '03':
        moves += 1
        if moves % 10**5 == 0: print(f'PROCESSING: {moves}')
        if modes[2] == '0': program[program[pos+1]] = inp
        if modes[2] == '1': program[pos+1] = inp
        if modes[2] == '2':
            program[rel + program[pos+1]] = inp
        pos += 2
    elif opcode == '04':
        out = first
        if out == 0:
            if inp == 1: grid[row-1,col] = 0
            elif inp == 2: grid[row+1,col] = 0
            elif inp == 3: grid[row,col-1] = 0
            elif inp == 4: grid[row,col+1] = 0
            else: print('ERROR');break
            inp = math.ceil((4*random()))
        elif out == 1:
            if inp == 1: grid[row-1,col] = 1;row -= 1
            elif inp == 2: grid[row+1,col] = 1;row += 1
            elif inp == 3: grid[row,col-1] = 1;col -= 1
            elif inp == 4: grid[row,col+1] = 1;col += 1
            else: print('ERROR');break
            inp = math.ceil((4*random()))
        elif out == 2:
            if inp == 1: grid[row-1,col] = 2;row -= 1
            elif inp == 2: grid[row+1,col] = 2;row += 1
            elif inp == 3: grid[row,col-1] = 2;col -= 1
            elif inp == 4: grid[row,col+1] = 2;col += 1
            else: print('ERROR');break
            # break
        else: print('ERROR');break
        pos += 2
    elif opcode == '05':
        if first == 0: pos += 3
        elif first != 0: pos = second
    elif opcode == '06':
        if first != 0: pos += 3
        elif first == 0: pos = second
    elif opcode == '07':
        if first < second: program[third] = 1
        else: program[third] = 0
        pos += 4
    elif opcode == '08':
        if first == second: program[third] = 1
        else: program[third] = 0
        pos += 4
    elif opcode == '09':
        rel += first
        pos += 2
    else: print('ERROR');break

print(moves)
