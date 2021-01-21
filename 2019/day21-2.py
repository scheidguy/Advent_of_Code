
from copy import deepcopy
# import numpy as np


f = open('day21-1_input.txt')
# f = open('day21-1_debug.txt')
text = f.readlines()
f.close()

program = [int(i) for i in text[0].strip().split(',')]
program.extend([0 for _ in range(10**4)])

outputs = []
inputs = []
asci = []
T = False
J = False
AND = [ord('A'), ord('N'), ord('D')]
OR = [ord('O'), ord('R')]
NOT = [ord('N'), ord('O'), ord('T')]
for L in 'ABC':
    instruction = deepcopy(NOT)
    instruction.extend([ord(' '),ord(L),ord(' '),ord('T'),10])
    inputs.append(instruction)
    instruction = deepcopy(OR)
    instruction.extend([ord(' '),ord('T'),ord(' '),ord('J'),10])
    inputs.append(instruction)
    
instruction = deepcopy(AND)
instruction.extend([ord(' '),ord('D'),ord(' '),ord('J'),10])
inputs.append(instruction)

instruction = deepcopy(AND)
instruction.extend([ord(' '),ord('H'),ord(' '),ord('J'),10])
inputs.append(instruction)

instruction = deepcopy(NOT)
instruction.extend([ord(' '),ord('A'),ord(' '),ord('T'),10])
inputs.append(instruction)

instruction = deepcopy(OR)
instruction.extend([ord(' '),ord('T'),ord(' '),ord('J'),10])
inputs.append(instruction)

inputs.append([ord('R'), ord('U'), ord('N'), 10])

pos = 0
rel = 0
out = 0
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
        if len(asci) == 0:
            asci = inputs.pop(0)
        inp = asci.pop(0)
        if modes[2] == '0': program[program[pos+1]] = inp
        if modes[2] == '1': program[pos+1] = inp
        if modes[2] == '2': program[rel + program[pos+1]] = inp
        pos += 2
    elif opcode == '04':
        out = first
        outputs.append(out)
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

if len(outputs) > 0:
    viz = ''
    for o in outputs[:-1]: viz += chr(o)
    print(viz)
