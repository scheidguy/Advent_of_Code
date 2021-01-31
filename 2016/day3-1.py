
f = open('day3_input.txt')
text = f.readlines()
f.close()

valid = 0
for line in text:
    line = line.strip()
    line = line.split('  ')
    nums = []
    for n in range(len(line)):
        if line[n] == ' ' or line[n] == '': continue
        nums.append(int(line[n]))
    if nums[0] < nums[1] + nums[2]:
        if nums[1] < nums[0] + nums[2]:
            if nums[2] < nums[1] + nums[0]:
                valid += 1

print(valid)
