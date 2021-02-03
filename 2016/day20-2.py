
f = open('day20_input.txt')
text = f.readlines()
f.close()

starts = []
stops = []
for line in text:
    line = line.strip()
    line = line.split('-')
    starts.append(int(line[0]))
    stops.append(int(line[1]))
    
num = 4294967296
# num = 10
while len(starts) > 0:
    startind = starts.index(min(starts))
    popinds = [startind]
    start = starts[startind]
    stop = stops[startind]
    foundone = True
    while foundone:
        foundone = False
        for i in range(len(starts)):
            if starts[i] <= stop:
                if stops[i] > stop:
                    foundone = True
                    stop = stops[i]
                    popinds.append(i)
                    break
                elif i not in popinds:
                    foundone = True
                    popinds.append(i)
                    break
    num -= stop - start + 1
    while len(popinds) > 0:
        starts.pop(max(popinds))
        stops.pop(max(popinds))
        popinds.pop(popinds.index(max(popinds)))

print(num)
