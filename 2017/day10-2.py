
f = open('day10_input.txt')
text = f.readlines()
f.close()

size = 256
for line in text:
    line = '1,2,3'
    lengths = [ord(entry) for entry in line.strip()]
lengths.extend([17, 31, 73, 47, 23])


curr = 0
skip = 0
thelist = list(range(size))
for rounds in range(64):
    for length in lengths:
        
        if curr + length <= size:
            sublist = thelist[0:curr]
            sublist.extend(thelist[curr:curr+length][::-1])
            if curr + length != size:
                sublist.extend(thelist[curr+length:])
            thelist = sublist
        else:
            reversi = thelist[curr:]
            reversi.extend(thelist[0:(curr+length) % size])
            aug = -1
            while len(reversi) > 0:
                aug += 1
                thelist[(curr+aug) % size] = reversi.pop()
        curr += skip + length
        curr %= size
        skip += 1

dense = []
for block in range(16):
    for entry in range(16):
        if entry == 0:
            num = thelist[16*block + entry]
        else:
            num ^= thelist[16*block + entry]
    dense.append(num)

knot = ''
for d in dense:
    h = hex(d)[2:]
    h = '0'*(2-len(h)) + h
    knot += h

print(knot)
