
from copy import deepcopy
import numpy as np


f = open('day19-1_input.txt')
# f = open('day19-1_debug.txt')
text = f.readlines()
f.close()

prog = [int(i) for i in text[0].strip().split(',')]
prog.extend([0 for _ in range(10**4)])

size = 50
grid = np.array([[' ' for _ in range(size)] for __ in range(size)])
for x in range(size):
    for y in range(size):
        program = deepcopy(prog)
        pos = 0
        rel = 0
        inp = 0
        out = 0
        inputs = [x, y]
        while True:
            command = str(program[pos])
            command = '0'*(5-len(command)) + command
            opcode = command[-2:]
            modes = command[0:-2]
            if opcode == '99': break
        
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
                inp = inputs.pop(0)
                if modes[2] == '0': program[program[pos+1]] = inp
                if modes[2] == '1': program[pos+1] = inp
                if modes[2] == '2': program[rel + program[pos+1]] = inp
                pos += 2
            elif opcode == '04':
                out = first
                if out == 0: grid[x, y] = '.'
                elif out == 1: grid[x, y] = '#'
                else: print('wat.')
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

print(len(np.where(grid == '#')[0]))
