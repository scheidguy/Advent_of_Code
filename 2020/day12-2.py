
f = open('day12-1_input.txt')
# f = open('day12-1_debug.txt')
text = f.readlines()
f.close()

x = 10
y = 1
shipx = 0
shipy = 0
for action in text:
    print(shipx,shipy)
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
        oldx = x
        oldy = y
        if val == 90:
            y = oldx
            x = -oldy
        if val == 180:
            y = -oldy
            x = -oldx
        if val == 270:
            y = -oldx
            x = oldy
    if direction == 'R':
        oldx = x
        oldy = y
        if val == 90:
            y = -oldx
            x = oldy
        if val == 180:
            y = -oldy
            x = -oldx
        if val == 270:
            y = oldx
            x = -oldy
    if direction == 'F':
        shipx += x * val
        shipy += y * val
print(abs(shipx) + abs(shipy))








