
from collections import deque


numelves = 458
nummarbles = 7202000
scores = [0 for elf in range(numelves)]
circle = deque([0, 1])
curr = 1
marble = 1
elf = 1
while marble < nummarbles - 1:
    marble += 1
    elf += 1
    if elf == numelves:
        elf = 0
    if marble % 23 != 0:
        circle.rotate(-2)
        circle.appendleft(marble)
    else:
        circle.rotate(7)
        scores[elf] += marble + circle.popleft()

print(max(scores))
