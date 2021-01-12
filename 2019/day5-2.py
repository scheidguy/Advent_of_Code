

f = open('day5-1_input.txt')
# f = open('day5-1_debug.txt')
text = f.readlines()
f.close()

program = [int(i) for i in text[0].strip().split(',')]

inp = 5
pos = 0
while True:
    command = str(program[pos])
    command = '0'*(5-len(command)) + command
    opcode = command[-2:]
    modes = command[0:-2]
    if opcode == '99': break

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
        if modes[2] == '0': program[program[pos+1]] = inp
        if modes[2] == '1': program[pos+1] = inp
        pos += 2
    elif opcode == '04':
        print(first)
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
    else: print('ERROR');break
        
    
