
f = open('day14_input.txt')
text = f.readlines()
f.close()

distances = [[] for _ in range(9)]
ind = -1
for line in text:
    line = line.strip()
    line = line.strip('.')
    line = line.split(' ')
    ind += 1
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
        distances[ind].append(distance)
        
points = [0 for _ in range(9)]
for time in range(2503):
    current = [distances[i][time] for i in range(9)]
    leader = current.index(max(current))
    points[leader] += 1

print(max(points))
