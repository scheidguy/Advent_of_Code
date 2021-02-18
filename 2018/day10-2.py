
import numpy as np


f = open('day10_input.txt')
text = f.readlines()
f.close()

xs = []
ys = []
vxs = []
vys = []
for line in text:
    line = line.strip()
    x = int(line[10:16])
    y = int(line[17:24])
    vx = int(line[-7:-5])
    vy = int(line[-3:-1])
    xs.append(x)
    ys.append(y)
    vxs.append(vx)
    vys.append(vy)

length = max(ys) - min(ys)
prev = 10**9
steps = 0
while length < prev:
    steps += 1
    prev = length
    for i in range(len(xs)):
        xs[i] += vxs[i]
        ys[i] += vys[i]
    length = max(ys) - min(ys)

for i in range(len(xs)):
        xs[i] -= vxs[i]
        ys[i] -= vys[i]

leftmost = min(xs)
topmost = min(ys)
for i in range(len(xs)):
    xs[i] -= leftmost
    ys[i] -= topmost

message = np.array([[' ' for _ in range(max(xs) + 1)] for __ in range(max(ys) + 1)])
for i in range(len(xs)):
    message[ys[i], xs[i]] = '#'

for row in range(message.shape[0]):
    print(''.join(message[row, :]))
print(steps)
