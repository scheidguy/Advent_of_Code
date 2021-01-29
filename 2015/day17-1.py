
from itertools import combinations


f = open('day17_input.txt')
text = f.readlines()
f.close()


containers = []
for line in text:
    line = line.strip()
    containers.append(int(line))

num = 0
for n in range(3,17):
    combos = combinations(list(range(20)), n)
    for com in combos:
        capacity = 0
        for ind in com:
            capacity += containers[ind]
        if capacity == 150: num += 1

print(num)
