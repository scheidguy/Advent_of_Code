
from itertools import combinations
from copy import deepcopy


f = open('day25-1_input.txt')
text = f.readlines()
f.close()
f = open('commands.txt')
commands = f.readlines()
f.close()
f = open('dropall.txt')
dropall = f.readlines()
f.close()

inputs = [[ord(letter) for letter in line] for line in commands]

drops = [[ord(letter) for letter in line] for line in dropall]

program = [int(i) for i in text[0].strip().split(',')]
program.extend([0 for _ in range(10**4)])

objects = ['jam','bowl of rice','antenna','manifold','hypercube','dehydrated water','candy cane','dark matter']
inventory = []
for r in range(2,len(objects)): inventory.extend(list(combinations(objects,r)))
messages = []
ejections = 0

pos = 0
rel = 0
inps = []
outputs = []
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
        if len(inputs) == 0 and len(inps) == 0:
            ejected = ['ejected' in messages[i] for i in range(-25,-10)]
            if any(ejected):
                inputs = deepcopy(drops)
                for item in inventory.pop():
                    inputs.append([])
                    inputs[-1].append(ord('t'))
                    inputs[-1].append(ord('a'))
                    inputs[-1].append(ord('k'))
                    inputs[-1].append(ord('e'))
                    inputs[-1].append(ord(' '))
                    inputs[-1].extend([ord(let) for let in item])
                    inputs[-1].append(10)
                inputs.append([])
                inputs[-1].append(ord('w'))
                inputs[-1].append(ord('e'))
                inputs[-1].append(ord('s'))
                inputs[-1].append(ord('t'))
                inputs[-1].append(10)
            else:
                print('wat.');break
        if len(inps) == 0:
            inps = inputs.pop(0)
        inp = inps.pop(0)
        if modes[2] == '0': program[program[pos+1]] = inp
        if modes[2] == '1': program[pos+1] = inp
        if modes[2] == '2': program[rel + program[pos+1]] = inp
        pos += 2
    elif opcode == '04':
        out = first
        if out == 10:
            messages.append(''.join(map(str, [chr(i) for i in outputs])))
            outputs = []
        else: outputs.append(out)
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

print(messages[-1])
