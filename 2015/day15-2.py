
f = open('day15_input.txt')
text = f.readlines()
f.close()

traits = [[] for _ in range(4)]
calories = []
trait = -1
for line in text:
    line = line.strip()
    line = line.replace(',','')
    line = line.split(' ')
    trait += 1
    traits[trait].append(int(line[2]))
    traits[trait].append(int(line[4]))
    traits[trait].append(int(line[6]))
    traits[trait].append(int(line[8]))
    calories.append(int(line[-1]))

highest = 0
for t1 in range(101):
    for t2 in range(101 - t1):
        for t3 in range(101 - t1 - t2):
            t4 = 100 - t1 - t2 - t3
            score = 1
            for trait in range(4):
                subscore = 0
                subscore += t1 * traits[0][trait]
                subscore += t2 * traits[1][trait]
                subscore += t3 * traits[2][trait]
                subscore += t4 * traits[3][trait]
                if subscore < 0: subscore = 0;break
                score *= subscore
            if subscore == 0: continue
            cals = 0
            cals += t1 * calories[0]
            cals += t2 * calories[1]
            cals += t3 * calories[2]
            cals += t4 * calories[3]
            if cals != 500: continue
            if score > highest: highest = score
            
print(highest)
            
    
