
inp = list(map(int, '1113222113'))

for process in range(40):
    newinp = []
    num = 0
    for i in range(len(inp)-1):
        num += 1
        if inp[i+1] == inp[i]: continue
        newinp.append(num)
        newinp.append(inp[i])
        num = 0
    num += 1
    newinp.append(num)
    newinp.append(inp[i+1])
    inp = newinp

print(len(inp))
