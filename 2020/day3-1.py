# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 21:51:59 2020

@author: schei
"""


f = open('day3-1_input.txt')
text = f.readlines()
f.close()

tree = 0

i = 0
col = 0
for entry in text:
    l = list(entry)
    if i == 0:
        i += 1
        continue
    col += 3
    if col > 30: col -= 31
    if l[col] == '#': tree += 1
    

print(tree)

