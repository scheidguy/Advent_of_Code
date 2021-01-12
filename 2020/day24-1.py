
f = open('day24-1_input.txt')
# f = open('day24-1_debug.txt')
text = f.readlines()
f.close()

num = 0
coords = []
for line in text:
    line = line.strip()
    x = 0
    y = 0
    skip = False
    for i in range(len(line)):
        if skip: skip = False;continue
        if line[i] == 'e': x += 1
        if line[i] == 'w': x -= 1
        if line[i] == 's':
            skip = True
            if line[i+1] == 'e':
                y -= round(3**0.5 / 2, 1)
                x += 0.5
            if line[i+1] == 'w':
                y -= round(3**0.5 / 2, 1)
                x -= 0.5
        if line[i] == 'n':
            skip = True
            if line[i+1] == 'e':
                y += round(3**0.5 / 2, 1)
                x += 0.5
            if line[i+1] == 'w':
                y += round(3**0.5 / 2, 1)
                x -= 0.5
    coord = (x, round(y,1))
    if coord in coords: coords.remove(coord)
    else: coords.append(coord)

print(len(coords))
        
