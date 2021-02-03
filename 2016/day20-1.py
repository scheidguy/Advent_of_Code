
f = open('day20_input.txt')
text = f.readlines()
f.close()

starts = []
stops = []
for line in text:
    line = line.strip()
    line = line.split('-')
    starts.append(int(line[0]))
    stops.append(int(line[1]))
    
IP = 0
blocked = True
while blocked:
    while IP in starts:
        IP = stops[starts.index(IP)] + 1
    blocked = False
    for i in range(len(starts)):
        if IP >= starts[i] and IP <= stops[i]:
            IP = stops[i] + 1
            blocked = True
            break

print(IP)
