

f = open('day1_input.txt')
text = f.readlines()
f.close()


for line in text:
    line = line.strip()
floor = 0
for letter in line:
    if letter == '(': floor += 1
    if letter == ')': floor -= 1
print(floor)
