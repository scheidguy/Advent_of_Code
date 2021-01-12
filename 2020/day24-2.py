
from copy import deepcopy


def numneighbors(coord, coords):
    bx = coord[0]
    by = coord[1]
    neighbors = 0
    if (round(bx-0.5,1), round(by-0.9,1)) in coords: neighbors += 1
    if (round(bx+0.5,1), round(by-0.9,1)) in coords: neighbors += 1
    if (round(bx-0.5,1), round(by+0.9,1)) in coords: neighbors += 1
    if (round(bx+0.5,1), round(by+0.9,1)) in coords: neighbors += 1
    if (round(bx-1.0,1), round(by,1)) in coords: neighbors += 1
    if (round(bx+1.0,1), round(by,1)) in coords: neighbors += 1
    return neighbors


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
    
for day in range(100):
    newcoords = deepcopy(coords)
    removeme = []
    for black in coords:
        num = numneighbors(black, coords)
        if num == 0 or num > 2:
            removeme.append(black)
    addme = []
    for black in coords:
        bx = black[0]
        by = black[1]
        test = [(bx-0.5, by-0.9), (bx+0.5, by-0.9), (bx-0.5, by+0.9), (bx+0.5, by+0.9), (bx-1.0, by), (bx+1.0, by)]
        for t in test:
            T = (round(t[0],1), round(t[1],1))
            if T not in coords:
                num = numneighbors(T, coords)
                if num == 2 and T not in addme: addme.append(T)
    for r in removeme: newcoords.remove(r)
    for a in addme: newcoords.append(a)
    coords = newcoords
    
print(len(coords))
        
