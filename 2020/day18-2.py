
import numpy as np
import copy
import math


f = open('day18-1_input.txt')
# f = open('day18-1_debug.txt')
text = f.readlines()
f.close()


def calc(ex):
    ops = []
    nums = []
    prods = []
    num = ''
    for i in range(len(ex)):
        if ex[i].isnumeric():
            num += ex[i]
        else:
            ops.append(ex[i])
            nums.append(int(num))
            num = ''
    nums.append(int(num))
    while '+' in ops:
        tally = 0
        for j in range(len(ops)):
            if ops[j] == '+':
                nums[j] = nums[j] + nums[j+1]
                nums.pop(j+1)
                ops.pop(j)
                break
    return str(math.prod(nums))


sumall = 0
for line in text:
    ex = line.strip().replace(' ','')
    stillparen = '(' in ex
    while stillparen:
        start = 10**9
        end = -1
        ind = -1
        for char in ex:
            ind += 1
            if char == '(': start = ind
            if char == ')': end = ind
            if end > start and ex[start+1:].find('(') == -1:
                if end == len(ex)-1: ex = ex[0:start] + calc(ex[start+1:end])
                else: ex = ex[0:start] + calc(ex[start+1:end]) + ex[end+1:]
                break
            elif end > start and end < (ex[start+1:].find('(') + start + 1):
                ex = ex[0:start] + calc(ex[start+1:end]) + ex[end+1:]
                break
            
        stillparen = '(' in ex
    add = int(calc(ex))
    sumall += add

print(sumall)
