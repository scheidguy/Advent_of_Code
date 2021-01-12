
f = open('day12-1_input.txt')
text = f.readlines()
f.close()

x = 0
y = 0
dirs = ['east', 'south', 'west', 'north']
currdir= dirs[0]
for action in text:
    val = int(action[1:])
    direction = action[0]
    if direction == 'N':
        y += val
    if direction == 'S':
        y -= val
    if direction == 'E':
        x += val
    if direction == 'W':
        x -= val
    if direction == 'L':
        if val == 90:
            if currdir == dirs[0]: currdir = dirs[-1]
            else: currdir = dirs[dirs.index(currdir) - 1]
        if val == 180:
            if currdir == dirs[0]: currdir = dirs[-2]
            elif currdir == dirs[1]: currdir = dirs[-1]
            else: currdir = dirs[dirs.index(currdir) - 2]
        if val == 270:
            if currdir == dirs[-1]: currdir = dirs[0]
            else: currdir = dirs[dirs.index(currdir) + 1]
    if direction == 'R':
        if val == 90:
            if currdir == dirs[-1]: currdir = dirs[0]
            else: currdir = dirs[dirs.index(currdir) + 1]
        if val == 180:
            if currdir == dirs[-1]: currdir = dirs[1]
            elif currdir == dirs[-2]: currdir = dirs[0]
            else: currdir = dirs[dirs.index(currdir) + 2]
        if val == 270:
            if currdir == dirs[0]: currdir = dirs[-1]
            else: currdir = dirs[dirs.index(currdir) - 1]
    if direction == 'F':
        if currdir == 'east': x += val
        if currdir == 'south': y -= val
        if currdir == 'west': x -= val
        if currdir == 'north': y += val
print(abs(x) + abs(y))








