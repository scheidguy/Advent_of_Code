
import numpy as np
from copy import deepcopy


f = open('day15_input.txt')
text = f.readlines()
f.close()

cave = []
coords = []
HP = []
races = []
row = -1
for line in text:
    row += 1
    line = line.strip()
    cave.append(list(line))
    col = -1
    for letter in line:
        col += 1
        if letter in 'EG':
            coords.append([row, col])
            HP.append(200)
            races.append(letter)

cave = np.array(cave, dtype=object)
rnd = -1
while True:
    rnd += 1
    killed = []
    order = [100*coords[i][0] + coords[i][1] for i in range(len(coords))]
    for unit in range(len(coords)):
        i = order.index(min(order))
        order[i] = 10**6
        if HP[i] == 0:
            continue
        race = races[i]
        row = coords[i][0]
        col = coords[i][1]
        up = cave[row-1, col]
        down = cave[row+1, col]
        left = cave[row, col-1]
        right = cave[row, col+1]
        if (race == 'E' and 'G' not in [up, down, left, right]) or (race == 'G' and 'E' not in [up, down, left, right]):
            distances = [10**6 for _ in range(4)]
            for directions in range(4):
                maze = deepcopy(cave)
                maze[row, col] = '0'
                maze[row-1, col] = '#'
                maze[row+1, col] = '#'
                maze[row, col-1] = '#'
                maze[row, col+1] = '#'
                if directions == 0 and cave[row-1, col] == '.':
                    maze[row-1, col] = '.'
                if directions == 1 and cave[row, col-1] == '.':
                    maze[row, col-1] = '.'
                if directions == 2 and cave[row, col+1] == '.':
                    maze[row, col+1] = '.'
                if directions == 3 and cave[row+1, col] == '.':
                    maze[row+1, col] = '.'
                steps = 0
                inds = np.where(maze == str(steps))
                rows = inds[0]
                cols = inds[1]
                foundone = False
                while len(rows) > 0:
                    steps += 1
                    for j in range(len(rows)):
                        r = rows[j]
                        c = cols[j]
                        if maze[r+1, c].isalpha() and maze[r+1, c] != race:
                            foundone = True
                            distances[directions] = steps - 1
                            break
                        if maze[r, c+1].isalpha() and maze[r, c+1] != race:
                            foundone = True
                            distances[directions] = steps - 1
                            break
                        if maze[r, c-1].isalpha() and maze[r, c-1] != race:
                            foundone = True
                            distances[directions] = steps - 1
                            break
                        if maze[r-1, c].isalpha() and maze[r-1, c] != race:
                            foundone = True
                            distances[directions] = steps - 1
                            break

                        if maze[r-1, c] == '.':
                            maze[r-1, c] = str(steps)
                        if maze[r+1, c] == '.':
                            maze[r+1, c] = str(steps)
                        if maze[r, c-1] == '.':
                            maze[r, c-1] = str(steps)
                        if maze[r, c+1] == '.':
                            maze[r, c+1] = str(steps)

                    if foundone: break
                    inds = np.where(maze == str(steps))
                    rows = inds[0]
                    cols = inds[1]

            mindist = min(distances)
            if mindist != 10**6:
                if distances.index(mindist) == 0:
                    cave[row, col] = '.'
                    cave[row-1, col] = race
                    coords[i][0] -= 1
                elif distances.index(mindist) == 1:
                    cave[row, col] = '.'
                    cave[row, col-1] = race
                    coords[i][1] -= 1
                elif distances.index(mindist) == 2:
                    cave[row, col] = '.'
                    cave[row, col+1] = race
                    coords[i][1] += 1
                elif distances.index(mindist) == 3:
                    cave[row, col] = '.'
                    cave[row+1, col] = race
                    coords[i][0] += 1

        row = coords[i][0]
        col = coords[i][1]
        up = cave[row-1, col]
        down = cave[row+1, col]
        left = cave[row, col-1]
        right = cave[row, col+1]
        enemies = []
        inds = []
        if (race == 'E' and up == 'G') or (race == 'G' and up == 'E'):
            ind = coords.index([row-1, col])
            inds.append(ind)
            enemies.append(HP[ind])
        if (race == 'E' and left == 'G') or (race == 'G' and left == 'E'):
            ind = coords.index([row, col-1])
            inds.append(ind)
            enemies.append(HP[ind])
        if (race == 'E' and right == 'G') or (race == 'G' and right == 'E'):
            ind = coords.index([row, col+1])
            inds.append(ind)
            enemies.append(HP[ind])
        if (race == 'E' and down == 'G') or (race == 'G' and down == 'E'):
            ind = coords.index([row+1, col])
            inds.append(ind)
            enemies.append(HP[ind])
        if len(enemies) > 0:
            targetind = inds[enemies.index(min(enemies))]
            HP[targetind] -= 3
            if HP[targetind] <= 0:
                HP[targetind] = 0
                killed.append(targetind)
                cave[coords[targetind][0], coords[targetind][1]] = '.'

    killed.sort()
    for removeme in killed[::-1]:
        coords.pop(removeme)
        HP.pop(removeme)
        races.pop(removeme)
    if len(set(races)) == 1:
        break

print(rnd * sum(HP))
