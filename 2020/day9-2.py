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


target = 138879426
vals = [int(line) for line in text]
for length in range(2, 100):
    for start in range(len(vals) - length):
        if sum(vals[start:start+length]) == target:
            print(min(vals[start:start+length]) + max(vals[start:start+length]))
            break
        