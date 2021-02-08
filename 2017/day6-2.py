
f = open('day6_input.txt')
text = f.readlines()
f.close()


banks = list(map(int, text[0].strip().split()))
SEEN = []
SEEN.append(''.join(list(map(str, banks))))
steps = 0
while True:
    steps += 1
    blocks = max(banks)
    biggest = banks.index(blocks)
    banks[biggest] = 0
    aug = 0
    while blocks > 0:
        aug += 1
        blocks -= 1
        banks[(biggest + aug) % len(banks)] += 1
    new = ''.join(list(map(str, banks)))
    if new not in SEEN:
        SEEN.append(new)
    else:
        break

print(steps - SEEN.index(new))

