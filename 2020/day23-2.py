
f = open('day23-1_input.txt')
# f = open('day23-1_debug.txt')
text = f.readlines()
f.close()

cups = {i:i+1 for i in range(1,10**6+1)}  # value is neighbor in clockwise dir
beginning = [int(c) for c in list(text[0].strip())]
for i in range(len(beginning) - 1):
    cups[beginning[i]] = beginning[i+1]
cups[beginning[-1]] = beginning[0]
cups[beginning[-1]] = 10
cups[10**6] = beginning[0]
    
curr = beginning[0]
for turn in range(10**7):
    if turn % 10**6 == 0: print(turn)

    first = cups[curr]
    second = cups[first]
    third = cups[second]
    cups[curr] = cups[third]
    
    cups.pop(first)
    cups.pop(second)
    cups.pop(third)
    
    dest = curr - 1
    while dest not in cups.keys():
        dest -= 1
        if dest < 1: dest = 10**6
    saveit = cups[dest]
    cups[dest] = first
    cups[first] = second
    cups[second] = third
    cups[third] = saveit
    curr = cups[curr]

print(cups[1] * cups[cups[1]])
