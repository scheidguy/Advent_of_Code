
f = open('day9_input.txt')
text = f.readlines()
f.close()


for line in text:
    line = line.strip()

decompressed = ''
ind = -1
while True:
    ind += 1
    if ind >= len(line):
        break
    char = line[ind]
    if char == '(':
        checkit = line[ind+1:ind+9]
        subsequent = ''
        reps = ''
        findreps = False
        good2go = False
        i = ind
        for c in checkit:
            i += 1
            if c == ')':
                if len(reps) > 0 and len(subsequent) > 0:
                    good2go = True
                break
            if c == 'x':
                findreps = True
            elif not c.isnumeric():
                good2go = False
                break
            elif findreps:
                reps += c
            else:
                subsequent += c
        if good2go:
            reps = int(reps)
            subsequent = int(subsequent)
            decompressed += reps * line[i+1:i+1+subsequent]
            ind = i + subsequent
    else:
        decompressed += char

print(len(decompressed))
