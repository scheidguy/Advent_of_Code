
import numpy as np


inp = 1352

size = 10**3
maze = 10**6 * np.ones((size, size))


for x in range(size):
    for y in range(size):
        binary = bin(x*x + 3*x + 2*x*y + y + y*y + inp)
        binary = binary[2:]
        numbits = sum(list(map(int, list(binary))))
        if numbits % 2 == 0:
            maze[x, y] = 0

maze[1, 1] = 1
steps = 1
while True:
    xinds = np.where(maze == steps)[0]
    yinds = np.where(maze == steps)[1]
    if len(xinds) == 0: break
    steps += 1
    for i in range(len(xinds)):
        x = xinds[i]
        y = yinds[i]
        if y > 0:
            if maze[x, y - 1] == 0: maze[x, y - 1] = steps
        if y < size - 1:
            if maze[x, y + 1] == 0: maze[x, y + 1] = steps
        if x > 0:
            if maze[x - 1, y] == 0: maze[x - 1, y] = steps
        if x < size - 1:
            if maze[x + 1, y] == 0: maze[x + 1, y] = steps

maze[maze == 0] = 10**5
print(len(np.where(maze <= 51)[0]))
