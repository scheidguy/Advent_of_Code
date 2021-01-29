
f = open('day19_input.txt')
text = f.readlines()
f.close()

molecule = text[-1]
replacements = {}
for line in text:
    line = line.strip()
    if line == '': break
    line = line.split(' => ')
    if line[0] in replacements.keys():
        replacements[line[0]].append(line[1])
    else:
        replacements[line[0]] = [line[1]]

SEEN = set()
for key in replacements.keys():
    for item in replacements[key]:
        for i in range(len(molecule)-1):
            if molecule[i:i+len(key)] == key:
                SEEN.add(molecule[0:i] + item + molecule[i+len(key):])
print(len(SEEN))
