
f = open('day11_input.txt')
text = f.readlines()
f.close()


for line in text:
    line = line.strip()

s = line.count('s,')
se = line.count('se')
sw = line.count('sw')
n = line.count('n,')
ne = line.count('ne')
nw = line.count('nw')

r3 = 3**0.5 / 2
y = n - s + ne/2 + nw/2 - se/2 - sw/2
x = r3*ne + r3*se - r3*nw - r3*sw 

print(round(x/r3) + y - round(x/r3)/2)
