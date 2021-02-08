
f = open('day7_input.txt')
text = f.readlines()
f.close()

towers = {}
weights = {}
for line in text:
    line = line.strip()
    line = line.replace(',','').split()
    tower = line[0]
    weight = line[1][1:-1]
    weights[tower] = int(weight)
    if len(line) > 2:
        towers[tower] = line[3:]
    else:
        towers[tower] = []

for tower1 in towers.keys():
    foundit = False
    for tower2 in towers.keys():
        if tower1 in towers[tower2]:
            foundit = True
            break
    if not foundit:
        break

print(tower1)
