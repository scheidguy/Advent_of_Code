
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
            else:
                output = int(line[6])
                outputs[output] = low
                if all(outputs[0:3]):
                    alldone = True
                    break
            if line[-2] == 'bot':
                highbot = int(line[-1])
                bots[highbot].append(high)
            else:
                output = int(line[-1])
                outputs[output] = high
                if all(outputs[0:3]):
                    alldone = True
                    break
    if alldone: break

print(outputs[0] * outputs[1] * outputs[2])
