

def decompress(line):
    decompressed = 0
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
                ind = i + subsequent
                substring = line[i+1:i+1+subsequent]
                if '(' in substring:
                    subsequent = decompress(substring)
                decompressed += reps * subsequent
            else:
                decompressed += 1
        else:
            decompressed += 1
    return decompressed


f = open('day9_input.txt')
text = f.readlines()
f.close()


for string in text:
    string = string.strip()

print(decompress(string))
