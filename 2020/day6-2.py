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

a = list(string.ascii_lowercase)

num = 0
for group in text:
    people = group.split('\n')
    alph = list(string.ascii_lowercase)
    size = 0
    for person in people:
        size += 1
        person = list(person)
        for letter in person:
            if letter in alph:alph.append(letter)
    for let in a:
        if alph.count(let) == size + 1: num += 1

print(num)
