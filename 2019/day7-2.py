
import copy
from itertools import permutations


f = open('day7-1_input.txt')
# f = open('day7-1_debug.txt')
text = f.readlines()
f.close()

P = [int(i) for i in text[0].strip().split(',')]

biggest = 0
phaseorders = list(permutations(range(5,10)))
for order in phaseorders:
    done = [False for _ in range(5)]
    posses = [0 for _ in range(5)]
    programs = [copy.deepcopy(P) for _ in range(5)]
    out = 0
    while not all(done):
        for amp in range(5):
            phase = order[amp]
            program = programs[amp]
            pos = posses[amp]
            while True:
                command = str(program[pos])
                command = '0'*(5-len(command)) + command
                opcode = command[-2:]
                modes = command[0:-2]
                if opcode == '99':
                    done[amp] = True
                    break
            
                if modes[2] == '0': first = program[program[pos+1]]
                if modes[2] == '1': first = program[pos+1]
                if opcode in ['01', '02', '05', '06', '07', '08']:
                    if modes[1] == '0': second = program[program[pos+2]]
                    if modes[1] == '1': second = program[pos+2]
                    if opcode in ['01', '02', '07', '08']:
                        if modes[0] == '0': third = program[pos+3]
                        if modes[0] == '1': third = pos+3
                
                if opcode == '01':
                    program[third] = first + second
                    pos += 4
                elif opcode == '02':
                    program[third] = first * second
                    pos += 4
                elif opcode == '03':
                    if pos == 0:  # first time through
                        if modes[2] == '0': program[program[pos+1]] = phase
                        if modes[2] == '1': program[pos+1] = phase
                    else:
                        if modes[2] == '0': program[program[pos+1]] = out
                        if modes[2] == '1': program[pos+1] = out
                    pos += 2
                elif opcode == '04':
                    out = first
                    pos += 2
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
                else: print('ERROR');break
            posses[amp] = pos
    if out > biggest: biggest = out

print(biggest)
    

