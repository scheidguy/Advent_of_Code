
f = open('day7_input.txt')
text = f.readlines()
f.close()

valid = 0
for line in text:
    line = line.strip()
    abba = False
    noabba = True
    hyper = False
    for i in range(3, len(line)):
        if line[i] == '[': hyper = True
        if line[i] == ']': hyper = False
        if line[i] == line[i-3] and line[i-1] == line[i-2] and line[i] != line[i-1]:
            if hyper:
                noabba = False
            else:
                abba = True
    if abba and noabba:
        valid += 1
    
print(valid)
