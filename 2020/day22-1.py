
f = open('day22-1_input.txt')
# f = open('day22-1_debug.txt')
text = f.readlines()
f.close()

firstdeck = True
for line in text:
    line = line.strip()
    if line == '': continue
    elif line == 'Player 1:': p1 = []
    elif line == 'Player 2:': p2 = [];firstdeck = False
    elif firstdeck: p1.append(int(line))
    elif not firstdeck: p2.append(int(line))

while len(p1) > 0 and len(p2) > 0:
    card1 = p1.pop(0)
    card2 = p2.pop(0)
    if card1 > card2: p1.append(card1);p1.append(card2)
    if card2 > card1: p2.append(card2);p2.append(card1)

score = 0
mult = 0
for i in range(1, len(p1) + 1):
    mult += 1
    score += p1[-i] * mult
print(score)

score = 0
mult = 0
for i in range(1, len(p2) + 1):
    mult += 1
    score += p2[-i] * mult
print(score)
