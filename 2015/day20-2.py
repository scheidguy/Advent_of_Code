
import numpy as np


inp = 29000000
houses = np.array([0 for _ in range(3*10**6)])
for elf in range(1, 3*10**6):
    houses[elf:elf*50+1:elf] += 11*elf

print(np.where(houses >= inp)[0][0])
