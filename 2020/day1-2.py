# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 09:49:38 2020

@author: schei
"""


f = open('day1-1_input.txt')
text = f.readlines()
f.close()

list1 = [int(i) for i in text]
inc = 0
for num1 in list1:
    inc += 1
    for num2 in list1[inc:]:
        for num3 in list1[inc+1:]:
            if num1 + num2 + num3 == 2020:
                print(f'{num1} x {num2} x {num3} = {num1 * num2 * num3}')
