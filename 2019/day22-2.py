
# from random import random
# import numpy as np
# import math
from copy import deepcopy
import time



tic = time.time()
f = open('day22-1_input.txt')
# f = open('day20-1_debug1.txt')
text = f.readlines()
f.close()


bigdeck = 119315717514047
shuffles = 101741582076661

length = 10007
answers2019 = []
answers2020 = []
deck = [n for n in range(length)]
for _ in range(100):
    for line in text:
        line = line.strip()
        if 'stack' in line:
            deck = deck[::-1]
        elif 'increment' in line:
            pos = 0
            newdeck = [-1 for _ in range(length)]
            i = 0
            inc = int(line[-2:])
            pos = 0
            while i < length:
                newdeck[pos] = deck[i]
                i += 1
                pos += inc
                if pos >= length: pos -= length
            deck = deepcopy(newdeck)
        elif 'cut' in line:
            cut = int(line[4:])
            newdeck = deepcopy(deck[cut:])
            newdeck.extend(deck[0:cut])
            deck = newdeck
    answers2020.append(deck[2020])
    answers2019.append(deck[2019])
    
toc = time.time()
print(f'TIME ELAPSED: {round(toc-tic)} seconds')
