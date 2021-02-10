
jump = 366
buffer = [0, 1]
pos = 1
for num in range(2, 2018):
    ind = jump % len(buffer)
    pos += ind
    pos %= len(buffer)
    pos += 1
    if pos > len(buffer):
        buffer.append(num)
    else:
        buffer.insert(pos, num)

print(buffer[buffer.index(2017) + 1])
