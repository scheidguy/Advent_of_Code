

f = open('day6-1_input.txt')
# f = open('day6-1_debug.txt')
text = f.readlines()
f.close()

orbits = {}
for line in text:
    line = line.strip().split(')')
    orbits[line[1]] = line[0]

num = 0
for key in orbits.keys():
    obj = orbits[key]
    num += 1
    while obj != 'COM':
        num += 1
        obj = orbits[obj]
print(num)
    
