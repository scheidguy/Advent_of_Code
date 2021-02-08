
f = open('day12_input.txt')
text = f.readlines()
f.close()

programs = {}
for line in text:
    line = line.strip().split(' <-> ')
    program = int(line[0])
    others = line[1].split(', ')
    programs[program] = list(map(int, others))

group = []
prevlength = len(group)
group.append(0)
while prevlength != len(group):
    prevlength = len(group)
    for i in range(len(group)):
        group.extend(programs[group[i]])
    group = list(set(group))

print(len(group))
