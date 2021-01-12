
import numpy as np
import math


f = open('day10-1_input.txt')
# f = open('day10-1_debug.txt')
text = f.readlines()
f.close()

field = []
for line in text:
    field.append(list(line.strip()))
field = np.array(field)

most = set()
for row in range(len(field[0,:])):
    for col in range(len(field[0,:])):
        if field[row,col] != '#': continue
        knightmoves = set()
        for r in range(len(field[0,:])):
            for c in range(len(field[0,:])):
                if field[r,c] != '#': continue
                if row == r and col == c: continue
                upshift = r - row
                rightshift = c - col
                gcd = math.gcd(upshift, rightshift)
                upshift = upshift // gcd
                rightshift = rightshift // gcd
                knightmoves.add((upshift, rightshift))
        if len(knightmoves) > len(most): most = knightmoves

print(len(most))

