
f = open('day12_input.txt')
text = f.readlines()
f.close()

for line in text:
    line = line.strip()

bookends = []
start = []
stop = []
for i in range(len(line)):
    char = line[i]
    if char == '{': start.append(i)
    if char == '}':
        stop.append(i)
        bookends.append((start.pop(), stop.pop()))

for start,stop in bookends:
    struct = eval(line[start:stop+1])
    if 'red' in struct.keys() or 'red' in struct.values():
        line = line[0:start] + '[' + '0'*(stop-start-1) + ']' + line[stop+1:]

n = ''
num = 0
for i in range(len(line)):
    if line[i].isnumeric():
        if line[i-1] == '-': n += '-'
        n += line[i]
    else:
        if len(n) > 0: 
            num += int(n)
        n = ''

print(num)
