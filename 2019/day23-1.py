
from copy import deepcopy
# import numpy as np


f = open('day23-1_input.txt')
# f = open('day23-1_debug.txt')
text = f.readlines()
f.close()

program = [int(i) for i in text[0].strip().split(',')]
program.extend([0 for _ in range(10**4)])
NIC = [deepcopy(program)for computer in range(50)]

inputs = [[network_address] for network_address in range(50)]
foundit = False
poss = [0 for network_address in range(50)]
rels = [0 for network_address in range(50)]
numpackets = -1
while True:
    numpackets += 1
    for comp in range(50):
        program = NIC[comp]
        outputs = []
        pos = poss[comp]
        rel = rels[comp]
        while True:
            command = str(program[pos])
            command = '0'*(5-len(command)) + command
            opcode = command[-2:]
            modes = command[0:-2]
            if opcode == '99':
                # print(out)
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
                if len(inputs[comp]) == 0: inp = -1
                else: inp = inputs[comp].pop(0)
                if modes[2] == '0': program[program[pos+1]] = inp
                if modes[2] == '1': program[pos+1] = inp
                if modes[2] == '2': program[rel + program[pos+1]] = inp
                pos += 2
                if len(inputs[comp]) % 2 == 0:
                    poss[comp] = pos
                    rels[comp] = rel
                    break
            elif opcode == '04':
                out = first
                outputs.append(out)
                pos += 2
                if len(outputs) == 3:
                    if outputs[0] == 255: print(outputs[2]);foundit=True;break
                    if outputs[0] < 0 or outputs[0] > 49: print(f'address: {outputs[0]}')
                    inputs[outputs[0]].append(outputs[1])
                    inputs[outputs[0]].append(outputs[2])
                    outputs = []
                    poss[comp] = pos
                    rels[comp] = rel
                    break
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
        if foundit: break
    if foundit: break
