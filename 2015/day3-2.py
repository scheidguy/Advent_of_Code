

f = open('day3_input.txt')
text = f.readlines()
f.close()

x = 0
y = 0
X = 0
Y = 0
SEEN = set()
SEEN.add((0,0))
for line in text:
    line = line.strip()
num = 0
for direction in line:
    if num % 2 == 0:
        if direction == '^': y += 1
        if direction == 'v': y -= 1
        if direction == '>': x += 1
        if direction == '<': x -= 1
        SEEN.add((x,y))
    else:
        if direction == '^': Y += 1
        if direction == 'v': Y -= 1
        if direction == '>': X += 1
        if direction == '<': X -= 1
        SEEN.add((X,Y))
    num += 1
print(len(SEEN))
    
