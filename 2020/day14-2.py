import random
import copy
import numpy as np
import time


tic = time.time()

f = open('day14-1_input.txt')
# f = open('day14-2_debug.txt')
text = f.readlines()
f.close()

vals = {}
coins = 0
for line in text:
    if 'mask' in line:
        mask = line.split('=')[-1].strip()
    else:
        ind = int(line.split(']')[0][4:])
        if ind > 10**5: print('wut')
        dec = int(line.split('=')[-1].strip())
        b = list(bin(ind)[2:])
        extra = 0
        while len(b) < len(mask): b.insert(0, '0')

        new = ''
        for i in range(len(b)):
            if mask[i] == '0': new += b[i]
            if mask[i] == '1': new += '1'
            if mask[i] == 'X': new += 'X'
            
        new = list(new)
        newcopy = copy.deepcopy(new)
        spots = new.count('X')
        addresses = []
        while len(addresses) < 2**spots:
            for i in range(len(new)):
                if new[i] == 'X':
                    coins += 1
                    r = random.random()
                    if r > 0.5: newcopy[i] = '1'
                    else: newcopy[i] = '0'
            if newcopy not in addresses: addresses.append(copy.deepcopy(newcopy))
            
            
            
        
        for a in addresses:
            add = '0b'
            for i in range(len(a)): add += a[i]
            
            vals[str(int(add, 2))] = dec

print(sum(vals.values()))
toc = time.time()
# print(toc-tic)
# print(coins)