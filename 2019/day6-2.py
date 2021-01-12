

f = open('day6-1_input.txt')
# f = open('day6-1_debug.txt')
text = f.readlines()
f.close()

orbits = {}
for line in text:
    line = line.strip().split(')')
    orbits[line[1]] = line[0]

obj = orbits['YOU']
you = [obj]
while obj != 'COM':
    obj = orbits[obj]
    you.append(obj)

obj = orbits['SAN']
san = [obj]
while obj != 'COM':
    obj = orbits[obj]
    san.append(obj)

parent = you[0]
ind = 0
while parent not in san:
    ind += 1
    parent = you[ind]

num = ind + san.index(parent)
print(num)

    
