
f = open('day14_input.txt')
text = f.readlines()
f.close()

longest = 0
for line in text:
    line = line.strip()
    line = line.strip('.')
    line = line.split(' ')
    speed = int(line[3])
    duration = int(line[6])
    rest = int(line[-2])
    distance = 0
    elapsed = 0
    for time in range(2503):
        elapsed += 1
        if elapsed <= duration:
            distance += speed
        if elapsed == duration + rest:
            elapsed = 0
    if distance > longest: longest = distance
        

print(longest)
