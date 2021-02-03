
f = open('day23_input.txt')
text = f.readlines()
f.close()

a = 7
b = c = d = 0
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
        if line[2] not in 'abcd':
            pos += 1
            continue
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
        line = line.split()
        if line[-1] == 'a': move = a
        elif line[-1] == 'b': move = b
        elif line[-1] == 'c': move = c
        elif line[-1] == 'd': move = d
        else: move = int(line[-1])
        if line[1] == 'a' and a: pos += move
        elif line[1] == 'b' and b: pos += move
        elif line[1] == 'c' and c: pos += move
        elif line[1] == 'd' and d: pos += move
        elif line[1].isnumeric() and line[1] != '0': pos += move
        else: pos += 1
    if 'tgl' in line:
        if line[-1] == 'a': tog = a + pos
        elif line[-1] == 'b': tog = b + pos
        elif line[-1] == 'c': tog = c + pos
        elif line[-1] == 'd': tog = d + pos
        if tog < 0 or tog >= len(text):
            pos += 1
            continue
        line = text[tog].strip()
        if 'inc' in line:
            text[tog] = 'dec' + text[tog][3:]
        if 'dec' in line or 'tgl' in line:
            text[tog] = 'inc' + text[tog][3:]
        if 'jnz' in line:
            text[tog] = 'cpy' + text[tog][3:]
        if 'cpy' in line:
            text[tog] = 'jnz' + text[tog][3:]
        pos += 1
            
print(a)
