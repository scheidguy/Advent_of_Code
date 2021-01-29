
f = open('day16_input.txt')
text = f.readlines()
f.close()

decoder = {}
decoder['children:'] = 3
decoder['cats:'] = 7
decoder['samoyeds:'] = 2
decoder['pomeranians:'] = 3
decoder['akitas:'] = 0
decoder['vizslas:'] = 0
decoder['goldfish:'] = 5
decoder['trees:'] = 3
decoder['cars:'] = 2
decoder['perfumes:'] = 1

sues = {}
suenum = 0
for line in text:
    line = line.strip()
    line = line.replace(',','')
    line = line.split(' ')
    suenum += 1
    trait1 = {}
    trait2 = {}
    trait3 = {}
    trait1[line[2]] = int(line[3])
    trait2[line[4]] = int(line[5])
    trait3[line[6]] = int(line[7])
    sues[suenum] = [trait1, trait2, trait3]

for s in range(1, 501):
    sue = sues[s]
    trait = list(sue[0].keys())[0]
    if decoder[trait] != sue[0][trait]: continue
    trait = list(sue[1].keys())[0]
    if decoder[trait] != sue[1][trait]: continue
    trait = list(sue[2].keys())[0]
    if decoder[trait] != sue[2][trait]: continue
    print(s)


