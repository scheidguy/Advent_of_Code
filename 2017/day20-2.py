
f = open('day20_input.txt')
text = f.readlines()
f.close()

positions = []
vels = []
accs = []
for line in text:
    line = line.strip().split(', ')
    for i in range(3):
        line[i] = line[i].split(',')
    for j in range(3):
        line[j][0] = int(line[j][0][3:])
        line[j][1] = int(line[j][1])
        line[j][2] = int(line[j][2][0:-1])
    positions.append(line[0])
    vels.append(line[1])
    accs.append(line[2])

for tick in range(10**3):
    collided = set()
    for particle in range(len(accs)):
        for coord in range(3):
            vels[particle][coord] += accs[particle][coord]
    for particle in range(len(vels)):
        for coord in range(3):
            positions[particle][coord] += vels[particle][coord]
        if positions[particle] in positions[0:particle]:
            collided.add(particle)
            collided.add(positions[0:particle].index(positions[particle]))
    collided = sorted(list(collided))[::-1]
    for collision in collided:
        positions.pop(collision)
        vels.pop(collision)
        accs.pop(collision)

print(len(vels))
