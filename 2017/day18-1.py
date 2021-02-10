
f = open('day18_input.txt')
text = f.readlines()
f.close()

duet = []
for line in text:
    line = line.strip().split()
    duet.append(line)
    
pos = 0
regs = 'abfip'
registers = [0 for reg in range(len(regs))]
while pos >= 0 and pos < len(duet):
    command = duet[pos]
    pos += 1
    if 'snd' in command:
        sound = registers[regs.index(command[1])]
    if 'set' in command:
        if (command[2].strip('-')).isnumeric():
            registers[regs.index(command[1])] = int(eval(command[2]))
        else:
            registers[regs.index(command[1])] = registers[regs.index(command[2])]
    if 'add' in command:
        if (command[2].strip('-')).isnumeric():
            registers[regs.index(command[1])] += int(eval(command[2]))
        else:
            registers[regs.index(command[1])] += registers[regs.index(command[2])]
    if 'mul' in command:
        if (command[2].strip('-')).isnumeric():
            registers[regs.index(command[1])] *= int(eval(command[2]))
        else:
            registers[regs.index(command[1])] *= registers[regs.index(command[2])]
    if 'mod' in command:
        if (command[2].strip('-')).isnumeric():
            registers[regs.index(command[1])] %= int(eval(command[2]))
        else:
            registers[regs.index(command[1])] %= registers[regs.index(command[2])]
    if 'rcv' in command:
        if (command[1].strip('-')).isnumeric():
            if int(eval(command[1])):
                break
        else:
            if registers[regs.index(command[1])]:
                break
    if 'jgz' in command:
        if (command[1].strip('-')).isnumeric():
            if int(command[1]) > 0:
                pos -= 1
                if (command[2].strip('-')).isnumeric():
                    pos += int(eval(command[2]))
                else:
                    pos += registers[regs.index(command[2])]
        else:
            if registers[regs.index(command[1])] > 0:
                pos -= 1
                if (command[2].strip('-')).isnumeric():
                    pos += int(eval(command[2]))
                else:
                    pos += registers[regs.index(command[2])]

print(sound)