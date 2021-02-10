
f = open('day16_input.txt')
text = f.readlines()
f.close()


for line in text:
    line = line.strip().split(',')

programs = list('abcdefghijklmnop')
for dance in line:
    if '/' in dance:
        dance = dance.split('/')
        if dance[0][0] == 'p':
            p1 = dance[0][1]
            p2 = dance[1]
            pos1 = programs.index(p1)
            pos2 = programs.index(p2)
            programs[pos1] = p2
            programs[pos2] = p1
        else:
            pos1 = int(dance[0][1:])
            pos2 = int(dance[1])
            p1 = programs[pos1]
            p2 = programs[pos2]
            programs[pos1] = p2
            programs[pos2] = p1
    else:
        num = int(dance[1:])
        new = programs[-num:]
        new.extend(programs[0:-num])
        programs = new

print(''.join(programs))
