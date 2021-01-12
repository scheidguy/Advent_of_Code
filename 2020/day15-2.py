
nums = [0,3,6]
# nums = [11,0,1,10,5,19]
prevturn = {i:(1+nums.index(i)) for i in nums}

prev = 0
for turn in range(len(nums)+1, 30000000):  # 30000000
    if turn % 10**6 == 0: print(turn)
    if prev not in prevturn.keys():
        prevturn[prev] = turn
        prev = 0
    else:
        elapsed = turn - prevturn[prev]
        prevturn[prev] = turn
        prev = elapsed

print(prev)
