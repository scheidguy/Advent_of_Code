

import math
from itertools import combinations


f = open('day24_input.txt')
text = f.readlines()
f.close()

weights = []
for line in text:
    line = line.strip()
    weights.append(int(line))

size = sum(weights) / 3
quantum = []
smallest = 1
while len(quantum) == 0:
    smallest += 1
    combos = combinations(weights, smallest)
    for combo in combos:
        if sum(combo) == size:
            quantum.append(math.prod(combo))

print(min(quantum))
