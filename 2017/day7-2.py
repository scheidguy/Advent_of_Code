

def calcweights(subtower, towers, weights):
    weight = weights[subtower]
    for t in towers[subtower]:
        weight += calcweights(t, towers, weights)
    return weight


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

subtower = tower1
balanced = False
while not balanced:
    root = subtower
    subweights = []
    for subtower in towers[root]:
        subweights.append(calcweights(subtower, towers, weights))
    if subweights.count(min(subweights)) == 1:
        subtower = towers[root][subweights.index(min(subweights))]
        delta = max(subweights) - min(subweights)
    elif subweights.count(max(subweights)) == 1:
        subtower = towers[root][subweights.index(max(subweights))]
        delta = min(subweights) - max(subweights)
    else:
        balanced = True

print(weights[root] + delta)
