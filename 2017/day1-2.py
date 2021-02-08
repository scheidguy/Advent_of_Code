
f = open('day1_input.txt')
text = f.readlines()
f.close()


for line in text:
    line = line.strip()

num = 0
for i in range(len(line)):
    halfway = (i + (len(line) // 2)) % len(line)
    if line[i] == line[halfway]:
        num += int(line[i])
print(num)
