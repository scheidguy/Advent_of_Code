
from copy import deepcopy


f = open('day21_input.txt')
text = f.readlines()
f.close()

scramble = list('abcdefgh')
for line in text:
    line = line.strip()
    new = deepcopy(scramble)
    if 'swap position' in line:
        line = line.split()
        x = int(line[2])
        y = int(line[-1])
        new[x] = scramble[y]
        new[y] = scramble[x]
    if 'swap letter' in line:
        line = line.split()
        x = line[2]
        y = line[-1]
        for i in range(len(scramble)):
            if scramble[i] == x:
                new[i] = y
            if scramble[i] == y:
                new[i] = x
    if 'rotate left' in line:
        line = line.split()
        rotate = int(line[-2])
        while rotate >= len(scramble):
            rotate -= len(scramble)
        new = deepcopy(scramble[rotate:])
        new.extend(deepcopy(scramble[0:rotate]))
    if 'rotate right' in line:
        line = line.split()
        rotate = int(line[-2])
        while rotate >= len(scramble):
            rotate -= len(scramble)
        new = deepcopy(scramble[-rotate:])
        new.extend(deepcopy(scramble[0:-rotate]))
    if 'rotate based' in line:
        line = line.split()
        rotate = scramble.index(line[-1])
        num = 1 + rotate
        if rotate >= 4:
            num += 1
        rotate = num
        while rotate >= len(scramble):
            rotate -= len(scramble)
        new = deepcopy(scramble[-rotate:])
        new.extend(deepcopy(scramble[0:-rotate]))
    if 'reverse' in line:
        line = line.split()
        x = int(line[-3])
        y = int(line[-1])
        new = deepcopy(scramble[0:x])
        reversi = deepcopy(scramble[x:y+1])
        reversi.reverse()
        new.extend(reversi)
        if y + 1 < len(scramble):
            new.extend(deepcopy(scramble[y+1:]))
    if 'move' in line:
        line = line.split()
        x = int(line[2])
        y = int(line[-1])
        letter = new.pop(x)
        new.insert(y, letter)
    scramble = new

print(''.join(scramble))
