
from time import time


tic = time()
size = 3014603
elves = [num for num in range(1, size + 1)]
elf = 0
numelves = size
while numelves > 1:
    killed = (elf + numelves // 2) % numelves
    elves.pop(killed)
    numelves -= 1
    if killed > elf:
        elf = (1 + elf) % numelves
    elif elf >= numelves:
        elf = 0

print(elves.pop())
print(round(time()-tic))
