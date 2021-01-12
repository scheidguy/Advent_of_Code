

f = open('day14-1_input.txt')
# f = open('day14-1_debug.txt')
text = f.readlines()
f.close()

vals = [0 for i in range(10**5)]

for line in text:
    if 'mask' in line:
        mask = line.split('=')[-1].strip()
    else:
        ind = int(line.split(']')[0][4:])
        if ind > 10**5: print('wut')
        dec = int(line.split('=')[-1].strip())
        b = list(bin(dec)[2:])
        extra = 0
        while len(b) < len(mask): b.insert(0, '0')

        new = '0b'
        for i in range(len(b)):
            if mask[i] == '0': new += '0'
            if mask[i] == '1': new += '1'
            if mask[i] == 'X': new += b[i]

        vals[ind] = int(new, 2)

print(sum(vals))