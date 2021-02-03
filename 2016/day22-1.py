
f = open('day22_input.txt')
text = f.readlines()
f.close()


nodes = {}
for line in text[2:]:
    line = line.strip()
    line = line.split()
    size = int(line[1][:-1])
    used = int(line[2][:-1])
    avail = int(line[3][:-1])
    use = int(line[4][:-1])
    node = line[0].split('-')
    node = node[1] + node[2]
    nodes[node] = [size, used, avail, use]

viable = 0
for A in nodes.keys():
    for B in nodes.keys():
        if A != B:
            if nodes[A][1] > 0:
                if nodes[A][1] <= nodes[B][2] and nodes[B][1] <= nodes[A][2]:
                    viable += 1

print(viable)
