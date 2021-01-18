
import time
import numpy as np


tic = time.time()
f = open('day16-1_input.txt')
# f = open('day16-1_debug.txt')
text = f.readlines()
f.close()

signal = text[0].strip()
# signal = '03036732577212944063491565474664'
inp = [int(digit) for digit in signal * 10000]
start = int(signal[0:7])
inp = inp[start:]
inp = np.array(inp[::-1])

phase = 0
while phase < 100:
    phase += 1
    sums = np.cumsum(inp)
    out = [sums[i] % 10 for i in range(len(inp))]
    inp = out
    if phase % 10 == 0: print(f'Processed phase {phase}')

inp = inp[::-1]
print(''.join(list(map(str, inp[0:8]))))
toc = time.time()
print(f'TOTAL TIME ELAPSED: {round(toc-tic)} seconds')
