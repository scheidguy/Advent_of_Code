# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 20:59:15 2020

@author: schei
"""

import numpy as np
import string

f = open('day7-1_input.txt')
text = f.readlines()
f.close()

yup = ['light gold', 'dark tomato', 'bright maroon', 'dull maroon', 'plaid indigo']


target = 'shiny gold'
bags = {}
C = []
parentsize = len(yup)
num = parentsize
for rule in text:
    contents = []
    line = rule.split(',')
    colors = line[0].split()
    color = colors[0] + ' ' + colors[1]
    i = 0
    for l in line:
        i += 1
        if i == 1: contents.append(colors[-3] + ' ' + colors[-2])
        else:
            section = l.split()
            contents.append(section[1] + ' ' + section[2])
    C.append(color)
    bags[color] = contents

stillgoing = True
prevlength = parentsize
while stillgoing:
    for parent in yup:
        for candidate in C:
            inside = bags[candidate]
            for individual in inside:
                if individual in yup and candidate not in yup: yup.append(candidate)
    if len(yup) == prevlength: stillgoing = False
    else: prevlength = len(yup)
print(prevlength)    
