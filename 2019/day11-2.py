
import numpy as np


f = open('day11-1_input.txt')
# f = open('day11-1_debug.txt')
text = f.readlines()
f.close()

program = [int(i) for i in text[0].strip().split(',')]
program.extend([0 for _ in range(10**5)])

size = 1000
painted = np.zeros((size,size))
color = np.zeros((size,size))
row = col = size // 2
color[row, col] = 1
direction = 90
again = False


pos = 0
rel = 0
while True:
    inp = color[row, col]
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
        if modes[2] == '0': program[program[pos+1]] = inp
        if modes[2] == '1': program[pos+1] = inp
        if modes[2] == '2':
            program[rel + program[pos+1]] = inp
        pos += 2
    elif opcode == '04':
        if not again:
            again = True
            out = first
            color[row, col] = out
            painted[row, col] = 1
        else:
            again = False
            out = first
            if out == 0: direction = (direction + 90) % 360
            elif out == 1: direction = (direction - 90) % 360
            if direction == 0: col += 1
            if direction == 90: row -= 1
            if direction == 180: col -= 1
            if direction == 270: row += 1
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

print(np.count_nonzero(painted))