
f = open('day5_input.txt')
text = f.readlines()
f.close()


for line in text:
    line0 = line.strip()

smallest = 10**6
for removeme in 'abcdefghijklmnopqrstuvwxyz':
    print(removeme)
    line = line0.replace(removeme, '')
    line = line.replace(removeme.upper(), '')
    prevlength = 0
    while len(line) != prevlength:
        prevlength = len(line)
        for i in range(len(line) - 1):
            if abs(ord(line[i]) - ord(line[i+1])) == 32:
                line = line[0:i] + line[i+2:]
                break
    if len(line) < smallest:
        smallest = len(line)

print(smallest)
