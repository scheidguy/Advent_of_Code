
f = open('day12_input.txt')
text = f.readlines()
f.close()

programs = {}
for line in text:
    line = line.strip().split(' <-> ')
    program = int(line[0])
    others = line[1].split(', ')
    programs[program] = list(map(int, others))

groups = []
for p in range(len(text)):
    group = []
    prevlength = len(group)
    group.append(p)
    while prevlength != len(group):
        prevlength = len(group)
        for i in range(len(group)):
            group.extend(programs[group[i]])
        group = list(set(group))
    if min(group) not in groups:
        groups.append(min(group))

print(len(groups))
