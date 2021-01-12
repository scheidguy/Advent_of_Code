
import numpy as np


f = open('day20-1_input.txt')
# f = open('day20-1_debug.txt')
text = f.readlines()
f.close()

tiles = {}
for line in text:
    line = line.strip()
    if 'Tile' in line:
        tile = []
        ID = int(line.split()[1][0:-1])
    elif line == '': tiles[ID] = np.array(tile)
    else: tile.append(list(line.strip()))

IDmult = 1
corners = []
for key1 in tiles.keys():
    tile = tiles[key1]
    sidematches = 0
    options = [tile[0,:].tolist(), tile[-1,:].tolist(), tile[:,0].tolist(), tile[:,-1].tolist()]
    for key2 in tiles.keys():
        if key1 == key2: continue  # obviously would match itself
        candtile = tiles[key2]
        cands = [candtile[0,:].tolist(), candtile[-1,:].tolist(), candtile[:,0].tolist(), candtile[:,-1].tolist()]
        matched = False
        for option in options:
            if option in cands or option[::-1] in cands:
                matched = True
                break
        if matched: sidematches += 1
    if sidematches < 3:
        corners.append(key1)
        IDmult *= key1

print(IDmult)
    