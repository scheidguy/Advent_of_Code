
f = open('day1_input.txt')
text = f.readlines()
f.close()


for line in text:
    line = line.strip()

num = 0
for i in range(1, len(line)):
    if line[i] == line[i-1]:
        num += int(line[i])
print(num + 5)
