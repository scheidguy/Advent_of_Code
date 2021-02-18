
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
secondsleft = [61+n for n in range(26)]
A = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
elves = 5
time = 0
available = ''
while any(secondsleft):
    time += 1
    for letter in A:
        if prereqs[letter] == [] and secondsleft[A.index(letter)] > 0:
            if letter not in available:
                available += letter
    for i in range(len(available)):
        if i == elves:
            break
        secondsleft[A.index(available[i])] -= 1
    for letter in A:
        if prereqs[letter] == [] and secondsleft[A.index(letter)] == 0:
            available = available.replace(letter, '')
            for key in prereqs.keys():
                if letter in prereqs[key]:
                    prereqs[key].pop(prereqs[key].index(letter))
    print(secondsleft)

# order = ''
# while len(order) < 26:
#     alph = newalph
#     for letter in alph:
#         if len(prereqs[letter]) == 0:
#             order += letter
#             newalph = newalph.replace(letter, '')
#             for key in prereqs.keys():
#                 if letter in prereqs[key]:
#                     prereqs[key].pop(prereqs[key].index(letter))
#             break

print(time)
