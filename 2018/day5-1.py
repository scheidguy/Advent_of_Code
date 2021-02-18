
f = open('day5_input.txt')
text = f.readlines()
f.close()


for line in text:
    line = line.strip()

prevlength = 0
while len(line) != prevlength:
    prevlength = len(line)
    for i in range(prevlength - 1):
        if abs(ord(line[i]) - ord(line[i+1])) == 32:
            line = line[0:i] + line[i+2:]
            break

print(len(line))
