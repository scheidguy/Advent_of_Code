
import numpy as np


size = 3014603
elves = np.ones(size, dtype=int)
while sum(elves) != 1:
    left = np.where(elves > 0)[0]
    even = len(left) % 2 == 0
    if even:
        elves[left[1:size:2]] = 0
    else:
        elves[left[1:size:2]] = 0
        elves[np.where(elves > 0)[0][0]] = 0

print(np.where(elves > 0)[0][0] + 1)
