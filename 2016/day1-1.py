
f = open('day1_input.txt')
text = f.readlines()
f.close()

x = y = 0
direction = 'N'
locations = [(0,0)]
for line in text:
    line = line.strip()
    line = line.split(', ')
    for move in line:
        rotate = move[0]
        dist = int(move[1:])
        if rotate == 'R':
            if direction == 'N':
                direction = 'E'
                x += dist
            elif direction == 'E':
                direction = 'S'
                y -= dist
            elif direction == 'S':
                direction = 'W'
                x -= dist
            elif direction == 'W':
                direction = 'N'
                y += dist

        elif rotate == 'L':
            if direction == 'N':
                direction = 'W'
                x -= dist
            elif direction == 'E':
                direction = 'N'
                y += dist
            elif direction == 'S':
                direction = 'E'
                x += dist
            elif direction == 'W':
                direction = 'S'
                y -= dist

        if (x,y) in locations: break
        locations.append((x,y))

print(abs(x)+abs(y))
