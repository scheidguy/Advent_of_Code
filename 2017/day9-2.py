
f = open('day9_input.txt')
text = f.readlines()
f.close()


for line in text:
    line = line.strip()

score = 0
group = 0
pos = -1
garbage = False
cancel = 0
while pos < len(line) - 1:
    pos += 1
    char = line[pos]
    if char == '!':
        pos += 1
        continue
    elif char == '{' and not garbage:
        group += 1
    elif char == '}' and not garbage:
        score += group
        group -= 1
    elif char == '<' and not garbage:
        garbage = True
        continue
    elif char == '>':
        garbage = False
        continue
    if garbage:
        cancel += 1

print(cancel)
