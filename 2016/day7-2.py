
f = open('day7_input.txt')
text = f.readlines()
f.close()

valid = 0
for line in text:
    line = line.strip()
    abas = set()
    babs = set()
    hyper = False
    for i in range(2, len(line)):
        if line[i] == '[':
            hyper = True
            start = i
        if line[i] == ']':
            hyper = False
            start = i
        if line[i] == line[i-2] and line[i] != line[i-1]:
            if hyper:
                babs.add((ord(line[i-1]), ord(line[i]), ord(line[i-1])))
            else:
                abas.add((ord(line[i]), ord(line[i-1]), ord(line[i])))
    if len(babs.intersection(abas)) > 0:
        valid += 1
    
print(valid)
