
f = open('day1_input.txt')
text = f.readlines()
f.close()

x = y = 0
alldone = False
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
                for inc in range(1, dist + 1):
                    if (x+inc,y) in locations:
                        print(abs(x+inc)+abs(y))
                        alldone = True
                    locations.append((x+inc,y))
                x += dist
            elif direction == 'E':
                direction = 'S'
                for inc in range(1, dist + 1):
                    if (x,y-inc) in locations:
                        print(abs(x)+abs(y-inc))
                        alldone = True
                    locations.append((x,y-inc))
                y -= dist
            elif direction == 'S':
                direction = 'W'
                for inc in range(1, dist + 1):
                    if (x-inc,y) in locations:
                        print(abs(x-inc)+abs(y))
                        alldone = True
                    locations.append((x-inc,y))
                x -= dist
            elif direction == 'W':
                direction = 'N'
                for inc in range(1, dist + 1):
                    if (x,y+inc) in locations:
                        print(abs(x)+abs(y+inc))
                        alldone = True
                    locations.append((x,y+inc))
                y += dist

        elif rotate == 'L':
            if direction == 'N':
                direction = 'W'
                for inc in range(1, dist + 1):
                    if (x-inc,y) in locations:
                        print(abs(x-inc)+abs(y))
                        alldone = True
                    locations.append((x-inc,y))
                x -= dist
            elif direction == 'E':
                direction = 'N'
                for inc in range(1, dist + 1):
                    if (x,y+inc) in locations:
                        print(abs(x)+abs(y+inc))
                        alldone = True
                    locations.append((x,y+inc))
                y += dist
            elif direction == 'S':
                direction = 'E'
                for inc in range(1, dist + 1):
                    if (x+inc,y) in locations:
                        print(abs(x+inc)+abs(y))
                        alldone = True
                    locations.append((x+inc,y))
                x += dist
            elif direction == 'W':
                direction = 'S'
                for inc in range(1, dist + 1):
                    if (x,y-inc) in locations:
                        print(abs(x)+abs(y-inc))
                        alldone = True
                    locations.append((x,y-inc))
                y -= dist

        if alldone: break 
