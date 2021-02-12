
f = open('day1_input.txt')
text = f.readlines()
f.close()

freq = 0
for line in text:
    line = line.strip()
    freq += int(line)
print(freq)
