
f = open('day10_input.txt')
text = f.readlines()
f.close()


for line in text:
    lengths = [int(entry) for entry in line.strip().split(',')]

size = 256
thelist = list(range(size))
curr = 0
skip = 0
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

print(thelist[0] * thelist[1])
