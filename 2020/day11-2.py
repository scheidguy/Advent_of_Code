import copy


def neighbors(R , C, grid):
    num = 0
    r = R; c = C
    while r > 0:  # north
        r -= 1
        if grid[r][c] == '#': num += 1; break
        if grid[r][c] == 'L': break
    r = R; c = C
    while r < len(grid)-1:  # south
        r += 1
        if grid[r][c] == '#': num += 1; break
        if grid[r][c] == 'L': break
    r = R; c = C
    while c > 0:  # west
        c -= 1
        if grid[r][c] == '#': num += 1; break
        if grid[r][c] == 'L': break
    r = R; c = C
    while c < len(grid[0])-1:  # east
        c += 1
        if grid[r][c] == '#': num += 1; break
        if grid[r][c] == 'L': break
    r = R; c = C
    while r > 0 and c > 0:  # northwest
        r -= 1; c -= 1
        if grid[r][c] == '#': num += 1; break
        if grid[r][c] == 'L': break
    r = R; c = C
    while r > 0 and c < len(grid[0])-1:  # northeast
        r -= 1; c += 1
        if grid[r][c] == '#': num += 1; break
        if grid[r][c] == 'L': break
    r = R; c = C
    while r < len(grid)-1 and c > 0:  # southwest
        r += 1; c -= 1
        if grid[r][c] == '#': num += 1; break
        if grid[r][c] == 'L': break
    r = R; c = C
    while r < len(grid)-1 and c < len(grid[0])-1:  # southeast
        r += 1; c += 1
        if grid[r][c] == '#': num += 1; break
        if grid[r][c] == 'L': break
    return num


f = open('day11-1_input.txt')
prevgrid = f.readlines()
f.close()

# encircle the grid with floor spaces to simplify processing
rows = len(prevgrid)
for i in range(rows):
    prevgrid[i] = '.' + prevgrid[i].strip() + '.'
cols = len(prevgrid[0])
prevgrid.append(cols * '.')
prevgrid.insert(0, cols * '.')
nowgrid = copy.deepcopy(prevgrid)
rows = len(prevgrid)

unstable = True
while unstable:
    for row in range(rows):
        for col in range(cols):
            seat = prevgrid[row][col]
            if seat == 'L':
                if row == 90 and col == 20:
                    print('')
                neigh = neighbors(row, col, prevgrid)
                if neigh == 0:
                    updated = list(nowgrid[row])
                    updated[col] = '#'
                    updated = "".join(updated)
                    nowgrid[row] = updated
            elif seat == '#':
                neigh = neighbors(row, col, prevgrid)
                if neigh >= 5:
                    updated = list(nowgrid[row])
                    updated[col] = 'L'
                    updated = "".join(updated)
                    nowgrid[row] = updated
    if prevgrid == nowgrid:
        unstable = False
        print(sum([row.count('#') for row in nowgrid]))
    else: prevgrid = copy.deepcopy(nowgrid)










