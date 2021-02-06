
f = open('day25_input.txt')
text = f.readlines()
f.close()

i = 0
clock = []
while sum(clock[0:100]) != 50:
    i += 1
    print(f'Testing {i}')
    a = i
    b = 0
    c = 0
    d = 0
    pos = 0
    clock = []
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
            
            if line[1] == 'a' and a == 0: pos += 1;continue
            elif line[1] == 'b' and b == 0: pos += 1;continue
            elif line[1] == 'c' and c == 0: pos += 1;continue
            elif line[1] == 'd' and d == 0: pos += 1;continue
            elif line[1] == '0': pos += 1;continue
            
            move = int(line[-1])
            
            if move == -2:
                d += b
                b = 0
                continue
                
            if move == -4:
                if line[1] == '1':
                    b -= c
                    c = 0
                    pos += 1
                    continue
                else:
                    if b == 0:
                        pos -= 4
                        continue
                    elif c < 0 or b < 0:
                        print('wat.')
                    elif c <= b:
                        b -= c
                        c = 0
                        continue
                    else:
                        c -= b
                        b = 0
                        pos -= 4
                        continue

            if move == -5:
                d += 362 * c
                b = 0
                c = 0
                continue

            if move == -7:
                a += b // 2
                if b % 2 != 0:
                    c = 1
                else:
                    c = 2
                b = 0
                pos += 1
                continue

            if move == -19:
                print([a, b, c, d])
                ok = -1
                break
            
            if move == -21:
                pass

            if line[1] == 'a' and a: pos += move
            elif line[1] == 'b' and b: pos += move
            elif line[1] == 'c' and c: pos += move
            elif line[1] == 'd' and d: pos += move
            elif line[1].isnumeric() and line[1] != '0': pos += move
            else: pos += 1
        if 'out' in line:
            if line[-1] == 'a': out = a
            elif line[-1] == 'b': out = b
            elif line[-1] == 'c': out = c
            elif line[-1] == 'd': out = d
            else: out = int(line[4:])
            # print(out)
            pos += 1
            if out != 1 and out != 0:
                break
            else:
                clock.append(out)
        # if len(clock) > 0:
        #     if len(clock) % 2 == 0 and clock[-1] == 1:
        #         continue
        #     elif len(clock) % 2 != 0 and clock[-1] == 0:
        #         continue
        #     elif len(clock) >= 100:
        #         break
        #     else:
        #         break

print(a)
