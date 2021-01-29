
f = open('day23_input.txt')
text = f.readlines()
f.close()

a = 0
b = 0
instructions = []
for line in text:
    line = line.strip()
    instructions.append(line)

pos = 0
while pos >= 0 and pos < len(instructions):
    instruct = instructions[pos]
    command = instruct[0:3]
    if command == 'hlf':
        register = instruct[4]
        if register == 'a': a /= 2
        if register == 'b': b /= 2
        pos += 1
    if command == 'tpl':
        register = instruct[4]
        if register == 'a': a *= 3
        if register == 'b': b *= 3
        pos += 1
    if command == 'inc':
        register = instruct[4]
        if register == 'a': a += 1
        if register == 'b': b += 1
        pos += 1
    if command == 'jmp':
        pos += int(instruct[4:])
    if command == 'jie':
        register = instruct[4]
        if register == 'a' and a % 2 == 0: pos += int(instruct[7:])
        elif register == 'b' and b % 2 == 0: pos += int(instruct[7:])
        else: pos += 1
    if command == 'jio':
        register = instruct[4]
        if register == 'a' and a == 1: pos += int(instruct[7:])
        elif register == 'b' and b == 1: pos += int(instruct[7:])
        else: pos += 1

print(b)
