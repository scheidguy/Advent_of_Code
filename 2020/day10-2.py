

import numpy as np
import math
import string

f = open('day10-1_input.txt')
text = f.readlines()
f.close()

jolts = [0]
for line in text:
    jolts.append(int(line))
    
jolts.sort()
jolts.append(max(jolts)+3)
i = 0
d1 = 0
d3 = 0
mult = 1


# Make list of adapters that are absolutely necessary (diff of 3)
idx = 1
short = [0]
length = len(short)
while idx < len(jolts):
    if jolts[idx] == max(jolts):
        if jolts[idx] - jolts[idx-1] == 3: 
            if jolts[idx-1] not in short: short.append(jolts[idx-1])
        short.append(jolts[idx])
        break
    prev = jolts[idx-1]
    curr = jolts[idx]
    nex = jolts[idx+1]
    if curr - prev == 3:
        if prev not in short:
            short.append(prev)
        short.append(curr)
    idx += 1

# jolts[25]=40
# short.pop(13)
# Find other less obvi necessary adapters, e.g. 1 and 6 are in [0,1,4,6,8,11]
idx = 1
inbetweens = []
prevshort = short[0]
for S in short:
    inbetweens = [v for v in jolts if v > prevshort and v < S]
    diff = S - prevshort
    if diff / 2 == len(inbetweens) + 1:
        for I in inbetweens:
            short.insert(short.index(S), I)
    prevshort = S


# Time to do a bunch of n-choose-k's now that we have a skeleton to work off of
numways = 1
prevshort = short[0]
for S in short:
    miniways = 0
    inbetweens = [v for v in jolts if v > prevshort and v < S]
    N = len(inbetweens)
    if N > 0:
        diff = S-prevshort
        if diff <= 3: minK = 0
        else: minK = diff // 3  # e.g. Need at least one if S-prev=4
        for K in range(minK, N+1):
            miniways += math.comb(N, K)  # N choose K
        numways *= miniways
    prevshort = S

print(numways)









