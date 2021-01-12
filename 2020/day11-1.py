import copy

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
                neighbors = prevgrid[row-1][col-1:col+2] + prevgrid[row+1][col-1:col+2] + prevgrid[row][col-1] + prevgrid[row][col+1]
                if '#' not in neighbors:
                    updated = list(nowgrid[row])
                    updated[col] = '#'
                    updated = "".join(updated)
                    nowgrid[row] = updated
            elif seat == '#':
                neighbors = prevgrid[row-1][col-1:col+2] + prevgrid[row+1][col-1:col+2] + prevgrid[row][col-1] + prevgrid[row][col+1]
                if neighbors.count('#') >= 4:
                    updated = list(nowgrid[row])
                    updated[col] = 'L'
                    updated = "".join(updated)
                    nowgrid[row] = updated
    if prevgrid == nowgrid:
        unstable = False
        print(sum([row.count('#') for row in nowgrid]))
    else: prevgrid = copy.deepcopy(nowgrid)
