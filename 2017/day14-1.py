
size = 256
inp = 'jxqlasbh-'
used = 0
rows = []
for row in range(128):
    lengths = [ord(letter) for letter in (inp+str(row))]
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
    r = ''
    for d in dense:
        h = hex(d)[2:]
        h = '0'*(2-len(h)) + h
        knot += h
        for digit in h:
            bits = bin(int(digit , 16))[2:]
            r += '0'*(4-len(bits)) + bits
            used += bits.count('1')
    rows.append(r)

print(used)
