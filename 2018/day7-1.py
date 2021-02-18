
f = open('day7_input.txt')
text = f.readlines()
f.close()

prereqs = {}
for line in text:
    line = line.strip().split()
    first = line[1]
    then = line[-3]
    if then in prereqs.keys():
        prereqs[then].append(first)
    else:
        prereqs[then] = [first]

# prereqs['C'] = []
prereqs['O'] = []
prereqs['P'] = []
prereqs['V'] = []
newalph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
order = ''
while len(order) < 26:
    alph = newalph
    for letter in alph:
        if len(prereqs[letter]) == 0:
            order += letter
            newalph = newalph.replace(letter, '')
            for key in prereqs.keys():
                if letter in prereqs[key]:
                    prereqs[key].pop(prereqs[key].index(letter))
            break

print(order)
