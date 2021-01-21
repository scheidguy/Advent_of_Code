
from copy import deepcopy


f = open('day22-1_input.txt')
# f = open('day20-1_debug1.txt')
text = f.readlines()
f.close()

length = 10007
deck = [n for n in range(length)]

for line in text:
    line = line.strip()
    if 'stack' in line:
        deck = deck[::-1]
    elif 'increment' in line:
        pos = 0
        newdeck = [-1 for _ in range(length)]
        i = 0
        inc = int(line[-2:])
        pos = 0
        while i < length:
            newdeck[pos] = deck[i]
            i += 1
            pos += inc
            if pos >= length: pos -= length
        deck = deepcopy(newdeck)
    elif 'cut' in line:
        cut = int(line[4:])
        newdeck = deepcopy(deck[cut:])
        newdeck.extend(deck[0:cut])
        deck = newdeck

print(deck.index(2019))
