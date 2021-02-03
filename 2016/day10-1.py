
f = open('day10_input.txt')
text = f.readlines()
f.close()

bots = {num:[] for num in range(10**3)}
outputs = [0 for num in range(10**3)]
for line in text:
    line = line.strip()
    line = line.split()
    if line[0] == 'value':
        bot = int(line[-1])
        value = int(line[1])
        bots[bot].append(value)

alldone = False
while not alldone:
    for line in text:
        line = line.strip()
        line = line.split()
        if line[0] == 'value': continue
        else:
            bot = int(line[1])
            if len(bots[bot]) != 2: continue
            low = min(bots[bot])
            high = max(bots[bot])
            bots[bot] = []
            if line[5] == 'bot':
                lowbot = int(line[6])
                bots[lowbot].append(low)
                if 17 in bots[lowbot] and 61 in bots[lowbot]:
                    alldone = True
                    foundbot = lowbot
                    break
            else:
                output = int(line[6])
                outputs[output] = low
            if line[-2] == 'bot':
                highbot = int(line[-1])
                bots[highbot].append(high)
                if 17 in bots[highbot] and 61 in bots[highbot]:
                    alldone = True
                    foundbot = highbot
                    break
            else:
                output = int(line[-1])
                outputs[output] = high
    if alldone: break

print(foundbot)
