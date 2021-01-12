# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 20:58:30 2020

@author: schei
"""


f = open('day3-1_input.txt')
text = f.readlines()
f.close()

tree1 = 0
i = 0
col = 0
for entry in text:
    l = list(entry)
    if i == 0:
        i += 1
        continue
    col += 3
    if col > 30: col -= 31
    if l[col] == '#': tree1 += 1

tree2 = 0
i = 0
col = 0
for entry in text:
    l = list(entry)
    if i == 0:
        i += 1
        continue
    col += 1
    if col > 30: col -= 31
    if l[col] == '#': tree2 += 1
    
tree3 = 0
i = 0
col = 0
for entry in text:
    l = list(entry)
    if i == 0:
        i += 1
        continue
    col += 5
    if col > 30: col -= 31
    if l[col] == '#': tree3 += 1
    
tree4 = 0
i = 0
col = 0
for entry in text:
    l = list(entry)
    if i == 0:
        i += 1
        continue
    col += 7
    if col > 30: col -= 31
    if l[col] == '#': tree4 += 1
    
tree5 = 0
i = 0
col = 0
for entry in text:
    l = list(entry)
    if i == 0:
        i += 1
        continue
    else: i += 1
    if i % 2 == 0:
        continue
    col += 1
    if col > 30: col -= 31
    if l[col] == '#': tree5 += 1


print(tree1 * tree2 * tree3 * tree4 * tree5)