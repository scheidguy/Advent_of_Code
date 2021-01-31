
f = open('day3_input.txt')
text = f.readlines()
f.close()

valid = 0
nums = []
for line in text:
    line = line.strip()
    line = line.split('  ')
    for n in range(len(line)):
        if line[n] == ' ' or line[n] == '': continue
        nums.append(int(line[n]))

tri = []
for col1 in range(0, len(nums), 3):
    tri.append(nums[col1])
    if len(tri) == 3:
        if tri[0] < tri[1] + tri[2]:
            if tri[1] < tri[0] + tri[2]:
                if tri[2] < tri[1] + tri[0]:
                    valid += 1
        tri = []

tri = []
for col2 in range(1, len(nums), 3):
    tri.append(nums[col2])
    if len(tri) == 3:
        if tri[0] < tri[1] + tri[2]:
            if tri[1] < tri[0] + tri[2]:
                if tri[2] < tri[1] + tri[0]:
                    valid += 1
        tri = []

tri = []
for col3 in range(2, len(nums), 3):
    tri.append(nums[col3])
    if len(tri) == 3:
        if tri[0] < tri[1] + tri[2]:
            if tri[1] < tri[0] + tri[2]:
                if tri[2] < tri[1] + tri[0]:
                    valid += 1
        tri = []

print(valid)
