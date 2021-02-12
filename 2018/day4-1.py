
f = open('day4_input_sorted.txt')
text = f.readlines()
f.close()

asleep = {}
guard = 0
for line in text:
    line = line.strip().split('	')
    time = int(line[0][-6:-4] + line[0][-3:-1])
    shift = line[1].split()
    if 'Guard' in shift:
        guard = int(shift[1][1:])
    elif 'asleep' in shift:
        start = time
    else:
        if guard not in asleep.keys():
            asleep[guard] = 0
        asleep[guard] += time - start

for k in asleep.keys():
    if asleep[k] == max(asleep.values()):
        sleepyhead = k
        break

asleep = {}
guard = 0
minutes = [0 for minute in range(60)]
for line in text:
    line = line.strip().split('	')
    time = int(line[0][-6:-4] + line[0][-3:-1])
    shift = line[1].split()
    if 'Guard' in shift:
        guard = int(shift[1][1:])
    elif 'asleep' in shift:
        start = time
    else:
        if guard not in asleep.keys():
            asleep[guard] = 0
        asleep[guard] += time - start
        if guard == sleepyhead:
            for minute in range(60):
                if time > minute and start <= minute:
                    minutes[minute] += 1

print(sleepyhead * minutes.index(max(minutes)))
