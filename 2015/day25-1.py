

import numpy as np


prev = 20151125
mult = 252533
div = 33554393
codes = np.zeros((10**4, 10**4), dtype=int)
row = 0
col = 0
codes[0, 0] = prev
while codes[2946, 3028] == 0:
    if row == 0:
        row = min(np.where(codes[:,0] == 0)[0])
        col = 0
    else:
        row -= 1
        col += 1
    newcode = (prev * mult) % div
    codes[row, col] = newcode
    prev = newcode

print(codes[2946, 3028])
