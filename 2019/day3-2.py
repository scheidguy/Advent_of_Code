
import numpy as np


f = open('day3-1_input.txt')
# f = open('day3-1_debug.txt')
text = f.readlines()
f.close()

wire1 = text[0].strip().split(',')
wire2 = text[1].strip().split(',')
grid = np.zeros((10**5 // 2, 10**5 // 2), dtype=bool)

xport = 10**5 // 4
yport = 10**5 // 4
for path in wire1:
    dist = int(path[1:])
    if path[0] == 'R':
        grid[xport:xport+dist+1, yport] = True
        xport += dist
    elif path[0] == 'L':
        grid[xport-dist:xport, yport] = True
        xport -= dist
    elif path[0] == 'U':
        grid[xport, yport-dist:yport] = True
        yport -= dist
    elif path[0] == 'D':
        grid[xport, yport:yport+dist+1] = True
        yport += dist
    if xport < 0 or xport >= 10**5 // 2 or yport < 0 or yport >= 10**5 // 2:
        print('Out of bounds!')
        break

xport = 10**5 // 4
yport = 10**5 // 4
manhat = grid.size
intersections = []
steps2 = []
sumsteps = 0
for path in wire2:
    dist = int(path[1:])
    if path[0] == 'R':
        for ind in range(1,dist+1):
            if grid[xport+ind, yport]:
                intersections.append((xport+ind, yport))
                steps2.append(sumsteps + ind)
                candidate = abs(xport+ind - 10**5//4) + abs(yport - 10**5//4)
                if candidate < manhat: manhat = candidate
        xport += dist
    elif path[0] == 'L':
        for ind in range(1,dist+1):
            if grid[xport-ind, yport]:
                intersections.append((xport-ind, yport))
                steps2.append(sumsteps + ind)
                candidate = abs(xport-ind - 10**5//4) + abs(yport - 10**5//4)
                if candidate < manhat: manhat = candidate
        xport -= dist
    elif path[0] == 'U':
        for ind in range(1,dist+1):
            if grid[xport, yport-ind]:
                intersections.append((xport, yport-ind))
                steps2.append(sumsteps + ind)
                candidate = abs(xport - 10**5//4) + abs(yport-ind - 10**5//4)
                if candidate < manhat: manhat = candidate
        yport -= dist
    elif path[0] == 'D':
        for ind in range(1,dist+1):
            if grid[xport, yport+ind]:
                intersections.append((xport, yport+ind))
                steps2.append(sumsteps + ind)
                candidate = abs(xport - 10**5//4) + abs(yport+ind - 10**5//4)
                if candidate < manhat: manhat = candidate
        yport += dist
    if xport < 0 or xport >= 10**5 // 2 or yport < 0 or yport >= 10**5 // 2:
        print('Out of bounds!')
        break
    sumsteps += dist

steps1 = []
for x,y in intersections:
    sumsteps = 0
    xport = 10**5 // 4
    yport = 10**5 // 4
    for path in wire1:
        dist = int(path[1:])
        if path[0] == 'R':
            for ind in range(1,dist+1):
                if xport+ind == x and yport == y: steps1.append(sumsteps + ind)
            xport += dist
        elif path[0] == 'L':
            for ind in range(1,dist+1):
                if xport-ind == x and yport == y: steps1.append(sumsteps + ind)
            xport -= dist
        elif path[0] == 'U':
            for ind in range(1,dist+1):
                if xport == x and yport-ind == y: steps1.append(sumsteps + ind)
            yport -= dist
        elif path[0] == 'D':
            for ind in range(1,dist+1):
                if xport == x and yport+ind == y: steps1.append(sumsteps + ind)
            yport += dist
        sumsteps += dist

lowest = grid.size
for ind in range(len(steps1)):
    howmany = steps1[ind] + steps2[ind] 
    if howmany < lowest: lowest = howmany

print(lowest)
