# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 21:51:59 2020

@author: schei
"""


f = open('day4-1_input.txt')
text = f.readlines()
f.close()

fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
copy = fields

num = 0
N = 0
valid = 0
for entry in text:
    if entry == '\n':
        if num >= 7: valid += 1
        N += 1
        num = 0
        copy = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
        continue
    line = entry.split(' ')
    i = 0
    for word in line:
        w = word.split(':')
        if w[0] in copy:
            num += 1
            copy.pop(copy.index(w[0]))    

print(valid)

