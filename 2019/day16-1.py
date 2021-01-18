
# from random import random
# import numpy as np
# import math


f = open('day16-1_input.txt')
# f = open('day16-1_debug.txt')
text = f.readlines()
f.close()

inp = [int(digit) for digit in text[0].strip()]
# inp = [int(digit) for digit in '80871224585914546619083218645595']
base = [0, 1, 0, -1]

phase = 0
while phase < 100:
    phase += 1
    out = []
    for pos in range(len(inp)):
        pattern = []
        while len(pattern) < len(inp) + 1:
            for repeat in range(len(base)):
                for _ in range(pos + 1):
                    pattern.append(base[repeat])
        pattern.pop(0)
        added = 0
        for pos2 in range(len(inp)):
            added += inp[pos2] * pattern[pos2]
        out.append(abs(added) % 10)
    inp = out

print(''.join(list(map(str, inp[0:8]))))
