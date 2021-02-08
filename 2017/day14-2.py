
import numpy as np


size = 256
inp = 'jxqlasbh-'
# inp = 'flqrgnkx-'
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
    rows.append(list(map(int, r)))

disk = np.array(rows)
regions = 1
yinds = np.where(disk == 1)[1]
xinds = np.where(disk == 1)[0]
while len(xinds) > 0:
    regions += 1
    disk[xinds[0], yinds[0]] = regions
    yinds = np.where(disk == regions)[1]
    xinds = np.where(disk == regions)[0]
    foundone = True
    while foundone:
        foundone = False
        for i in range(len(xinds)):
            x = xinds[i]
            y = yinds[i]
            if x > 0:
                if disk[x-1, y] == 1:
                    disk[x-1, y] = regions
                    foundone = True
            if y > 0:
                if disk[x, y-1] == 1:
                    disk[x, y-1] = regions
                    foundone = True
            if x < len(disk[0, :]) - 1:
                if disk[x+1, y] == 1:
                    disk[x+1, y] = regions
                    foundone = True
            if y < len(disk[0, :]) - 1:
                if disk[x, y+1] == 1:
                    disk[x, y+1] = regions
                    foundone = True
        yinds = np.where(disk == regions)[1]
        xinds = np.where(disk == regions)[0]
    yinds = np.where(disk == 1)[1]
    xinds = np.where(disk == 1)[0]
            
print(regions - 1)
