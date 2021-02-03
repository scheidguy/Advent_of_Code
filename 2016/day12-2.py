
f = open('day12_input.txt')
text = f.readlines()
f.close()

a = b = d = 0
c = 1
pos = 0
while pos < len(text):
    line = text[pos].strip()
    if 'inc' in line:
        if line[-1] == 'a': a += 1
        if line[-1] == 'b': b += 1
        if line[-1] == 'c': c += 1
        if line[-1] == 'd': d += 1
        pos += 1
    if 'dec' in line:
        if line[-1] == 'a': a -= 1
        if line[-1] == 'b': b -= 1
        if line[-1] == 'c': c -= 1
        if line[-1] == 'd': d -= 1
        pos += 1
    if 'cpy' in line:
        line = line.split()
        if line[2] == 'a':
            if line[1] == 'a': a = a
            elif line[1] == 'b': a = b
            elif line[1] == 'c': a = c
            elif line[1] == 'd': a = d
            else: a = int(line[1])
        if line[2] == 'b':
            if line[1] == 'a': b = a
            elif line[1] == 'b': b = b
            elif line[1] == 'c': b = c
            elif line[1] == 'd': b = d
            else: b = int(line[1])
        if line[2] == 'c':
            if line[1] == 'a': c = a
            elif line[1] == 'b': c = b
            elif line[1] == 'c': c = c
            elif line[1] == 'd': c = d
            else: c = int(line[1])
        if line[2] == 'd':
            if line[1] == 'a': d = a
            elif line[1] == 'b': d = b
            elif line[1] == 'c': d = c
            elif line[1] == 'd': d = d
            else: d = int(line[1])
        pos += 1
    if 'jnz' in line:
        if line[4] == 'a' and a: pos += int(line[-2:])
        elif line[4] == 'b' and b: pos += int(line[-2:])
        elif line[4] == 'c' and c: pos += int(line[-2:])
        elif line[4] == 'd' and d: pos += int(line[-2:])
        elif line[4].isnumeric() and line[4] != '0': pos += int(line[-2:])
        else: pos += 1

print(a)
