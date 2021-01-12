

f = open('day1-1_input.txt')
# f = open('day1-1_debug.txt')
text = f.readlines()
f.close()

total = 0
for line in text:
    line = int(line.strip())
    total += (line // 3) - 2
    
