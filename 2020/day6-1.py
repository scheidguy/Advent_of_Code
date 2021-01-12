# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 20:57:26 2020

@author: schei
"""


import numpy as np
import string

f = open('day6-1_input.txt')
text = f.read()
text = text.split('\n\n')
f.close()

num = 0
for group in text:
    people = group.split('\n')
    alph = list(string.ascii_lowercase)
    for person in people:
        person = list(person)
        for letter in person:
            if letter in alph:
                num += 1
                alph.pop(alph.index(letter))

print(num)
