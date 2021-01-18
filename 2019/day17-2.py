
import numpy as np


f = open('day17-1_input.txt')
# f = open('day17-1_debug.txt')
text = f.readlines()
f.close()

program = [int(i) for i in text[0].strip().split(',')]
program.extend([0 for _ in range(10**5)])
program[0] = 2

f = open('day17-1_scaffold.txt')  # Saved from part 1
text = f.readlines()
f.close()
grid = np.array([[' ' for _ in range(79)] for __ in range(43)])
slot = 0
for line in text:
    slot += 1
    grid[slot, 1:78] = list(line.strip())
row = np.where(grid == '^')[0][0]
col = np.where(grid == '^')[1][0]
fullpath = 'R'
orientation = 'East'
steps = 0
while len(np.where(grid == '#')[0] > 1):
    grid[row][col] = '8'
    if orientation == 'East':
        if grid[row][col+1] == '#' or grid[row][col+1] == '8':
            col += 1
            steps += 1
        else:
            fullpath += ',' + str(steps)
            steps = 0
            if grid[row+1][col] == '#':
                orientation = 'South'
                fullpath += ',R'
            elif grid[row-1][col] == '#':
                orientation = 'North'
                fullpath += ',L'
    if orientation == 'West':
        if grid[row][col-1] == '#' or grid[row][col-1] == '8':
            col -= 1
            steps += 1
        else:
            fullpath += ',' + str(steps)
            steps = 0
            if grid[row+1][col] == '#':
                orientation = 'South'
                fullpath += ',L'
            elif grid[row-1][col] == '#':
                orientation = 'North'
                fullpath += ',R'
    if orientation == 'North':
        if grid[row-1][col] == '#' or grid[row-1][col] == '8':
            row -= 1
            steps += 1
        else:
            fullpath += ',' + str(steps)
            steps = 0
            if grid[row][col+1] == '#':
                orientation = 'East'
                fullpath += ',R'
            elif grid[row][col-1] == '#':
                orientation = 'West'
                fullpath += ',L'
    if orientation == 'South':
        if grid[row+1][col] == '#' or grid[row+1][col] == '8':
            row += 1
            steps += 1
        else:
            fullpath += ',' + str(steps)
            steps = 0
            if grid[row][col+1] == '#':
                orientation = 'East'
                fullpath += ',L'
            elif grid[row][col-1] == '#':
                orientation = 'West'
                fullpath += ',R'

# By inspection of fullpath:
a = 'R,6,L,10,R,8,R,8'
b = 'R,12,L,8,L,10'
c = 'R,12,L,10,R,6,L,10'
rout = 'A,B,A,C,B,C,A,B,A,C'
routine = [ord(char) for char in rout]
A = [ord(char) for char in a]
B = [ord(char) for char in b]
C = [ord(char) for char in c]
routine.append(10)
A.append(10)
B.append(10)
C.append(10)
inputs = [routine, A, B, C, [110, 10]]

pos = 0
rel = 0
inp = 0
while True:
    command = str(program[pos])
    command = '0'*(5-len(command)) + command
    opcode = command[-2:]
    modes = command[0:-2]
    if opcode == '99':
        print(out)
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
        inp = inputs[0].pop(0)
        if inp == 10: inputs.pop(0)
        if modes[2] == '0': program[program[pos+1]] = inp
        if modes[2] == '1': program[pos+1] = inp
        if modes[2] == '2': program[rel + program[pos+1]] = inp
        pos += 2
    elif opcode == '04':
        out = first
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
