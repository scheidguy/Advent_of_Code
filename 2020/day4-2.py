# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 21:51:59 2020

@author: schei
"""


import numpy as np

f = open('day4-1_input.txt')
# f = open('day4-1_input_valid.txt')
# f = open('day4-1_input_invalid.txt')
text = f.readlines()
f.close()

al = list('abcdef0123456789')
nums = list('0123456789')
eyes = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
copy = fields

num = 0
N = 0
valid = 0
for entry in text:
    if entry == '\n' or entry == 'scheid':
        if num >= 7: valid += 1
        N += 1
        num = 0
        copy = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
        continue
    line = entry.split()
    i = 0
    for word in line:
        w = word.split(':')
        if w[0] in copy:
            #num += 1
            copy.pop(copy.index(w[0]))
            if w[0] == 'byr':
                if int(w[1]) >= 1920 and int(w[1]) <= 2002: num += 1
            if w[0] == 'iyr':
                if int(w[1]) >= 2010 and int(w[1]) <= 2020: num += 1
            if w[0] == 'eyr':
                if int(w[1]) >= 2020 and int(w[1]) <= 2030: num += 1
            if w[0] == 'hgt':
                code = list(w[1])
                if code[-2] + code[-1] == 'cm':
                    h = int(w[1].split('cm')[0])
                    if h >= 150 and h <= 193: num += 1
                elif code[-2] + code[-1] == 'in':
                    h = int(w[1].split('in')[0])
                    if h >= 59 and h <= 76: num += 1
                else:
                    print('da fuck')
            if w[0] == 'hcl':
                if w[1] == '#623a2f':
                    print('DAYUM')
                code = list(w[1])
                if code[0] == '#' and len(code) == 7:
                    good = True
                    for i in range(1, 7):
                        if code[i] not in al: good = False
                    if good: num +=1
            if w[0] == 'ecl':
                if w[1] in eyes: num += 1
            if w[0] == 'pid':
                code = list(w[1])
                if len(code) == 9:
                    good = True
                    for digit in code:
                        if digit not in nums: good = False
                    if good: num += 1
                    
print(valid)
