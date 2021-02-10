
f = open('day18_input.txt')
text = f.readlines()
f.close()

duet = []
for line in text:
    line = line.strip().split()
    duet.append(line)
    
pos = 0
pos1 = 0
regs = 'abfip'
registers = [0 for reg in range(len(regs))]
registers1 = [0 for reg in range(len(regs))]
registers1[-1] = 1
stillrunning = [True, True]
numsent = 0
q0 = []
q1 = []
while all(stillrunning):
    if stillrunning[0]:
        waiting = False
        command = duet[pos]
        pos += 1
        if 'snd' in command:
            q1.append(registers[regs.index(command[1])])
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
            if len(q0) == 0:
                pos -= 1
                waiting = True
            else:
                registers[regs.index(command[1])] = q0.pop(0)
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
        if pos < 0 or pos >= len(duet):
            stillrunning[0] = False

    if stillrunning[1]:
        command = duet[pos1]
        pos1 += 1
        if 'snd' in command:
            q0.append(registers1[regs.index(command[1])])
            numsent += 1
        if 'set' in command:
            if (command[2].strip('-')).isnumeric():
                registers1[regs.index(command[1])] = int(eval(command[2]))
            else:
                registers1[regs.index(command[1])] = registers1[regs.index(command[2])]
        if 'add' in command:
            if (command[2].strip('-')).isnumeric():
                registers1[regs.index(command[1])] += int(eval(command[2]))
            else:
                registers1[regs.index(command[1])] += registers1[regs.index(command[2])]
        if 'mul' in command:
            if (command[2].strip('-')).isnumeric():
                registers1[regs.index(command[1])] *= int(eval(command[2]))
            else:
                registers1[regs.index(command[1])] *= registers1[regs.index(command[2])]
        if 'mod' in command:
            if (command[2].strip('-')).isnumeric():
                registers1[regs.index(command[1])] %= int(eval(command[2]))
            else:
                registers1[regs.index(command[1])] %= registers1[regs.index(command[2])]
        if 'rcv' in command:
            if len(q1) == 0:
                pos1 -= 1
                if len(q1) == 0 and len(q0) == 0 and waiting:
                    break
            else:
                registers1[regs.index(command[1])] = q1.pop(0)
        if 'jgz' in command:
            if (command[1].strip('-')).isnumeric():
                if int(command[1]) > 0:
                    pos1 -= 1
                    if (command[2].strip('-')).isnumeric():
                        pos1 += int(eval(command[2]))
                    else:
                        pos1 += registers1[regs.index(command[2])]
            else:
                if registers1[regs.index(command[1])] > 0:
                    pos1 -= 1
                    if (command[2].strip('-')).isnumeric():
                        pos1 += int(eval(command[2]))
                    else:
                        pos1 += registers1[regs.index(command[2])]
        if pos1 < 0 or pos1 >= len(duet):
            stillrunning[1] = False

print(numsent)
