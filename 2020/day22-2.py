
from copy import deepcopy


f = open('day22-1_input.txt')
# f = open('day22-1_debug.txt')
text = f.readlines()
f.close()


def play(p1, p2):
    orders1 = []
    orders2 = []
    while len(p1) > 0 and len(p2) > 0:
        if p1 in orders1 and p2 in orders2: return 1
        if p1 not in orders1: orders1.append(deepcopy(p1))
        if p2 not in orders2: orders2.append(deepcopy(p2))
        card1 = p1.pop(0)
        card2 = p2.pop(0)
        if len(p1) < card1 or len(p2) < card2:
            if card1 > card2: p1.append(card1);p1.append(card2)
            if card2 > card1: p2.append(card2);p2.append(card1)
        else:
            winner = play(p1[0:card1], p2[0:card2])
            if winner == 1: p1.append(card1);p1.append(card2)
            if winner == 2: p2.append(card2);p2.append(card1)
    if len(p1) == 0: return 2
    if len(p2) == 0: return 1


firstdeck = True
for line in text:
    line = line.strip()
    if line == '': continue
    elif line == 'Player 1:': p1 = []
    elif line == 'Player 2:': p2 = [];firstdeck = False
    elif firstdeck: p1.append(int(line))
    elif not firstdeck: p2.append(int(line))

winner = play(p1, p2)
if winner == 1:
    score = 0
    mult = 0
    for i in range(1, len(p1) + 1):
        mult += 1
        score += p1[-i] * mult
    print(score)

if winner == 2:
    score = 0
    mult = 0
    for i in range(1, len(p2) + 1):
        mult += 1
        score += p2[-i] * mult
    print(score)
