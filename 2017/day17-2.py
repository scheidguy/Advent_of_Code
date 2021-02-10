
jump = 366
pos = 1
for num in range(2, 50*10**6 + 1):
    ind = jump % num
    pos += ind
    pos %= num
    pos += 1
    if pos == 1:
        val = num

print(val)
