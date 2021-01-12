

import numpy as np
import string

f = open('day10-1_input.txt')
text = f.readlines()
f.close()

jolts = []
for line in text:
    jolts.append(int(line))
    
jolts.sort()
jolts.insert(0, 0)
jolts.append(max(jolts)+3)
i = 0
d1 = 0
d3 = 0
for j in jolts:
    if i < 1 or i > 1000:
        i += 1
        continue
    if j - jolts[i-1] == 1: d1 += 1
    elif j - jolts[i-1] == 3: d3 += 1
    i += 1
print(d1*(d3))
