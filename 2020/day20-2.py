
import numpy as np
from copy import deepcopy


f = open('day20-1_input.txt')
upperleft = 3217
# f = open('day20-1_debug.txt')  # ALSO uncomment lines 9 and 29 if debugging
# upperleft = 1951
text = f.readlines()
f.close()

tiles = {}
for line in text:
    line = line.strip()
    if 'Tile' in line:
        tile = []
        ID = int(line.split()[1][0:-1])
    elif line == '':
        tiles[ID] = np.array(tile)
        continue
    else:
        tile.append(list(line.strip()))

dim = int(len(tiles) ** 0.5)
jig = np.array([['!' for _ in range(dim*10)] for __ in range(dim*10)])
# upper left from part 1
jig[0:10,0:10] = np.rot90(np.rot90(tiles[upperleft]))
# jig[0:10,0:10] = np.flipud(tiles[upperleft])
tiles.pop(upperleft)
for col in range(dim):
    for row in range(dim):
        if col == 0 and row == 0: continue  # already initialized with upper left
        matches = {}
        for k in tiles:
            tile = tiles[k]
            options = [tile[0,:].tolist(), tile[-1,:].tolist(), tile[:,0].tolist(), tile[:,-1].tolist()]
            if col == 0: findme = jig[10*row-1, col*10:(col+1)*10].tolist()
            else: findme = jig[row*10:(row+1)*10, 10*col-1].tolist()
            if findme in options:
                if col == 0:  # matching to bottom of previous tile
                    if options.index(findme) == 0: reoriented = tile
                    if options.index(findme) == 1: reoriented = np.flipud(tile)
                    if options.index(findme) == 2: reoriented = np.rot90(np.fliplr(tile))
                    if options.index(findme) == 3: reoriented = np.rot90(tile)
                else:  # matching to right side of tile to the left
                    if options.index(findme) == 0: reoriented = np.rot90(np.fliplr(tile))
                    if options.index(findme) == 1: reoriented = np.rot90(np.rot90(np.rot90(tile)))
                    if options.index(findme) == 2: reoriented = tile
                    if options.index(findme) == 3: reoriented = np.fliplr(tile)
                matches[k] = reoriented
            if findme[::-1] in options:
                if col == 0:  # matching to bottom of previous tile
                    if options.index(findme[::-1]) == 0: reoriented = np.fliplr(tile)
                    if options.index(findme[::-1]) == 1: reoriented = np.rot90(np.rot90(tile))
                    if options.index(findme[::-1]) == 2: reoriented = np.rot90(np.rot90(np.rot90(tile)))
                    if options.index(findme[::-1]) == 3: reoriented = np.rot90(np.flipud(tile))
                else:  # matching to right side of tile to the left
                    if options.index(findme[::-1]) == 0: reoriented = np.rot90(tile)
                    if options.index(findme[::-1]) == 1: reoriented = np.rot90(np.flipud(tile))
                    if options.index(findme[::-1]) == 2: reoriented = np.flipud(tile)
                    if options.index(findme[::-1]) == 3: reoriented = np.rot90(np.rot90(tile))
                matches[k] = reoriented
        if len(matches) == 1:
            matchID = list(matches.keys())[0]
            jig[10*row:10*row+10, col*10:(col+1)*10] = matches[matchID]
            tiles.pop(matchID)
        else: print('uh oh')

jig = np.delete(jig, [n*10 for n in range(dim)], 0)
jig = np.delete(jig, [(n+1)*9-1 for n in range(dim)], 0)
jig = np.delete(jig, [n*10 for n in range(dim)], 1)
jig = np.delete(jig, [(n+1)*9-1 for n in range(dim)], 1)

monster1 = '                  # '
monster2 = '#    ##    ##    ###'
monster3 = ' #  #  #  #  #  #   '
m1 = [c == '#' for c in monster1]
m2 = [c == '#' for c in monster2]
m3 = [c == '#' for c in monster3]

numfound = 0
attempts = 0
while numfound == 0:
    attempts += 1
    if attempts == 5: jig = np.flipud(jig)
    jig = np.rot90(jig)
    for v in range(jig.shape[0] - len(monster1) + 1):  # moving vertically
        for h in range(jig.shape[1] - 3 + 1):  # moving horizontally
            found = True
            for i in range(len(m1)):
                if m1[i] and jig[h, v+i] != '#': found = False;break
            for i in range(len(m2)):
                if m2[i] and jig[h+1, v+i] != '#': 
                    found = False
                    break
            for i in range(len(m3)):
                if m3[i] and jig[h+2, v+i] != '#': 
                    found = False
                    break
            if found:
                numfound += 1
                for i in range(len(m1)):
                    if m1[i] and jig[h, v+i] == '#': jig[h, v+i] = '!'
                for i in range(len(m2)):
                    if m2[i] and jig[h+1, v+i] == '#': jig[h+1, v+i] = '!'
                for i in range(len(m3)):
                    if m3[i] and jig[h+2, v+i] == '#': jig[h+2, v+i] = '!'
        
print(sum(sum(np.char.count(jig, '#'))))
        
