
f = open('day1_input.txt')
text = f.readlines()
f.close()

freq = 0
SEEN = set()
SEEN.add(freq)
notdone = True
while notdone:
    for line in text:
        line = line.strip()
        freq += int(line)
        if freq not in SEEN:
            SEEN.add(freq)
        else:
            print(freq)
            notdone = False
            break
