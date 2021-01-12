
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
for row in range(len(field[:,0])):
    for col in range(len(field[0,:])):
        if field[row,col] != '#': continue
        knightmoves = set()
        for r in range(len(field[:,0])):
            for c in range(len(field[0,:])):
                if field[r,c] != '#': continue
                if row == r and col == c: continue
                upshift = row - r
                rightshift = c - col
                gcd = math.gcd(upshift, rightshift)
                upshift = upshift // gcd
                rightshift = rightshift // gcd
                knightmoves.add((upshift, rightshift))
        if len(knightmoves) > len(most): 
            most = knightmoves
            coord = (row, col)

angle = []
most = list(most)
for asteroid in most:
    up = asteroid[0]
    right = asteroid[1]
    if right == 0 and up > 0: angle.append(0)
    elif right == 0 and up < 0: angle.append(180)
    elif up == 0 and right > 0: angle.append(90)
    elif up == 0 and right < 0: angle.append(270)
    elif right > 0 and up > 0:
        angle.append((math.atan(abs(right / up))) * 180/math.pi)
    elif right > 0 and up < 0:
        angle.append((math.pi/2 + math.atan(abs(up / right))) * 180/math.pi)
    elif right < 0 and up < 0:
        angle.append((math.pi + math.atan(abs(right / up))) * 180/math.pi)
    elif right < 0 and up > 0:
        angle.append((3*math.pi/2 + math.atan(abs(up / right))) * 180/math.pi)

destroyed = 0
while True:
    small = min(angle)
    nextone = angle.index(small)
    x = most[nextone][1] + coord[1]
    y = coord[0] - most[nextone][0]
    angle[nextone] = 10**6
    destroyed += 1
    if destroyed == 200: break

print(100*x + y)
