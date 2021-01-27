

f = open('day1_input.txt')
text = f.readlines()
f.close()


for line in text:
    line = line.strip()
floor = 0
pos = 0
for letter in line:
    pos += 1
    if letter == '(': floor += 1
    if letter == ')': floor -= 1
    if floor < 0: break
print(pos)
