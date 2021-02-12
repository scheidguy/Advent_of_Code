
f = open('day23_input.txt')
text = f.readlines()
f.close()

duet = []
for line in text:
    line = line.strip().split()
    duet.append(line)
    
pos = 0
regs = 'abcdefgh'
registers = [0 for reg in range(len(regs))]
registers[0] = 1
while pos >= 0 and pos < len(duet):
    command = duet[pos]
    pos += 1
    if 'set' in command:
        if command[1] == 'f':
            okay = True
        if (command[2].strip('-')).isnumeric():
            registers[regs.index(command[1])] = int(eval(command[2]))
        else:
            registers[regs.index(command[1])] = registers[regs.index(command[2])]
    if 'sub' in command:
        if (command[2].strip('-')).isnumeric():
            registers[regs.index(command[1])] -= int(eval(command[2]))
        else:
            registers[regs.index(command[1])] -= registers[regs.index(command[2])]
    if 'mul' in command:
        if (command[2].strip('-')).isnumeric():
            registers[regs.index(command[1])] *= int(eval(command[2]))
        else:
            registers[regs.index(command[1])] *= registers[regs.index(command[2])]
    if 'jnz' in command:
        if command[2] == '-8':
            okay = True
            if (registers[1] / registers[3]).is_integer():
                registers[5] = 0
            registers[4] += abs(registers[-2])
            registers[-2] = 0
            continue
        if command[2] == '-23': # and registers[-2] == -17:
            print(registers)
        if (command[1].strip('-')).isnumeric():
            if int(command[1]) != 0:
                pos -= 1
                if (command[2].strip('-')).isnumeric():
                    pos += int(eval(command[2]))
                else:
                    pos += registers[regs.index(command[2])]
        else:
            if registers[regs.index(command[1])] != 0:
                pos -= 1
                if (command[2].strip('-')).isnumeric():
                    pos += int(eval(command[2]))
                else:
                    pos += registers[regs.index(command[2])]

print(registers[-1])
