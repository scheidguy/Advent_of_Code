
f = open('day11_input.txt')
text = f.readlines()
f.close()


s = 0
sw = 0
se = 0
n = 0
ne = 0
nw = 0
r3 = 3**0.5 / 2
farthest = 0
for line in text:
    line = line.strip().split(',')
    for step in line:
        if step == 's': s += step.count('s')
        if step == 'n': n += step.count('n')
        se += step.count('se')
        sw += step.count('sw')
        ne += step.count('ne')
        nw += step.count('nw')

        y = n - s + ne/2 + nw/2 - se/2 - sw/2
        x = r3*ne + r3*se - r3*nw - r3*sw
        
        distance = round(round(x/r3) + y - round(x/r3)/2)
        if distance > farthest:
            farthest = distance

print(farthest)
