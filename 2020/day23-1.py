
f = open('day23-1_input.txt')
# f = open('day23-1_debug.txt')
text = f.readlines()
f.close()

cups = [int(c) for c in list(text[0].strip())]
    
curr = 0
for turn in range(100):
    print(cups)
    label = cups[curr]
    pickup = []
    for _ in range(1, 4):
        ind = curr + 1
        if ind >= len(cups): pickup.append(cups.pop(0))
        else: pickup.append(cups.pop(ind))
    dest = label - 1
    while cups.count(dest) == 0:
        dest -= 1
        if dest < 1: dest = 9
    here = cups.index(dest)
    while len(pickup) > 0: cups.insert(here + 1, pickup.pop())
    curr = cups.index(label) + 1
    if curr == 9: curr = 0

print(cups)
