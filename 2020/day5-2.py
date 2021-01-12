# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 20:56:59 2020

@author: schei
"""


import numpy as np

f = open('day5-1_input.txt')
text = f.readlines()
f.close()

# text = ['FBFBBFFRLR']

biggest = 0
smallest = 10000
seats = []
for board in text:
    b = list(board)
    
    begin1 = 1
    begin2 = 1
    end2 = 128
    end1 = 8
    i = 0
    for letter in b:
        i += 1
        if i < 8:
            if letter == 'F':
                end2 -= 128/(2**i)
                if i == 7: row = end2
            elif letter == 'B':
                begin2 += 128/(2**i)
                if i == 7: row = begin2
        else:
            if letter == 'L':
                end1 -= 8/(2**(i-7))
                if i == 10: col = end1
            elif letter == 'R':
                begin1 += 8/(2**(i-7))
                if i == 10: col = begin1
    seat = 8*(row-1) + (col-1)
    seats.append(seat)
    if seat >= biggest: biggest = seat
    if seat <= smallest: smallest = seat
    
seats.sort()
j = 0
for s in seats:
    j += 1
    if seats[j] - s == 2: print(s+1)