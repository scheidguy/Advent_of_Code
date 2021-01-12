
# nums = [0,3,6]
nums = [11,0,1,10,5,19]

for turn in range(len(nums), 2020):
    prev = nums[turn-1]
    if nums.count(prev) == 1:
        nums.append(0)
    else:
       nums.append(1 + nums[:-1][::-1].index(prev))

print(nums[-1])
