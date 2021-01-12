# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 20:59:15 2020

@author: schei
"""

import numpy as np
import string

f = open('day9-1_input.txt')
text = f.readlines()
f.close()

block = []
for i in range(25): block.append(int(text[i]))

for i in range(25, len(text)):
    num = int(text[i])
    good = False
    for first in block:
        for second in block:
            if first >= second: continue
            if first + second == num:
                good = True
                break
        if good: break
    if good:
        block.pop(0)
        block.append(num)
    else:
        print(num)
        break
