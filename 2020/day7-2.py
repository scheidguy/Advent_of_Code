f = open('day7-1_input.txt')
text = f.readlines()
f.close()
target = 'shiny gold'
bags = {}
num = {}
C = []
for rule in text:
    contents = []
    line = rule.split(',')
    colors = line[0].split()
    color = colors[0] + ' ' + colors[1]
    i = 0
    for l in line:
        i += 1
        if i == 1: contents.append(colors[-4] + ' ' + colors[-3] + ' ' + colors[-2])
        else:
            section = l.split()
            contents.append(section[0] + ' ' + section[1] + ' ' + section[2])
    C.append(color)
    bags[color] = contents
    num[color] = 0
    if contents[0] == 'contain no other': num[color] = 1

for i in range(1000):
    for bag in bags.keys():
        if num[bag] > 0: continue
        allclear = True
        for kid in bags[bag]:
            kid = kid.split()
            mult = int(kid[0])
            kid = kid[1] + ' ' + kid[2]
            if num[kid] == 0:
                num[bag] = 0
                allclear = False
                break
            else: num[bag] += mult * num[kid]
        if allclear:
            if bag == target: print(num[bag])
            num[bag] += 1  # need to count itself  
