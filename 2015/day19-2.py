
import random

f = open('day19_input.txt')
text = f.readlines()
f.close()

molecule = text[-1]
replacements = {}
vals = []
for line in text:
    line = line.strip()
    if line == '': break
    line = line.split(' => ')
    if line[0] in replacements.keys():
        replacements[line[0]].append(line[1])
        vals.append(line[1])
    else:
        replacements[line[0]] = [line[1]]
        vals.append(line[1])

num = 0
keys = list(replacements.keys())
while molecule != 'e':
    ind = random.randint(0, len(vals)-1)
    removeme = vals[ind]
    if removeme not in molecule: continue
    num += 1
    if num % 25 == 0: print(num)
    for key in keys:
        if removeme in replacements[key]:
            molecule = molecule.replace(removeme, key, 1)
            break

print(num)

# SEEN = set()
# for key in replacements.keys():
#     for item in replacements[key]:
#         for i in range(len(molecule)-1):
#             if molecule[i:i+len(key)] == key:
#                 SEEN.add(molecule[0:i] + item + molecule[i+len(key):])
# print(len(SEEN))
