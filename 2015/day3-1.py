

f = open('day3_input.txt')
text = f.readlines()
f.close()

x = 0
y = 0
SEEN = set()
SEEN.add((0,0))
for line in text:
    line = line.strip()
for direction in line:
    if direction == '^': y += 1
    if direction == 'v': y -= 1
    if direction == '>': x += 1
    if direction == '<': x -= 1
    SEEN.add((x,y))
print(len(SEEN))
    
