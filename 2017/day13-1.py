
f = open('day13_input.txt')
text = f.readlines()
f.close()

depths = []
ranges = []
for line in text:
    line = line.strip().split(': ')
    depths.append(int(line[0]))
    ranges.append(int(line[1]))

time = -1
depth = -1
severity = 0
while depth <= max(depths):
    depth += 1
    time += 1
    if depth in depths:
        ind = depths.index(depth)
        if time % (2*(ranges[ind] - 1)) == 0:
            severity += depth * ranges[ind]

print(severity)
