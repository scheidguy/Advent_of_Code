# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 21:51:59 2020

@author: schei
"""


f = open('day2-1_input.txt')
text = f.readlines()
f.close()

valid = 0
for entry in text:
    entry = entry.split(' ')
    code = entry[0].split('-')
    letter = list(entry[1])[0]
    password = list(entry[2])
    num = 0
    for let in password:
        if let == letter: num += 1
    if num >= int(code[0]) and num <= int(code[1]): valid += 1
