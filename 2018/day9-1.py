
numelves = 458
nummarbles = 72020
scores = [0 for elf in range(numelves)]
circle = [0, 1]
curr = 1
marble = 1
elf = 1
while marble < nummarbles - 1:
    marble += 1
    elf += 1
    if elf == numelves:
        elf = 0
    if marble % 23 != 0:
        curr += 2
        if curr > len(circle):
            curr %= len(circle)
        circle.insert(curr, marble)
    else:
        curr -= 7
        if curr < 0:
            curr += len(circle)
        scores[elf] += marble + circle.pop(curr)

print(max(scores))
