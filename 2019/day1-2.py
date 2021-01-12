

f = open('day1-1_input.txt')
# f = open('day1-1_debug.txt')
text = f.readlines()
f.close()

total = 0
for line in text:
    line = int(line.strip())
    module = (line // 3) - 2
    prev = module
    while True:
        div = (prev // 3) - 2
        if div <= 0: break
        module += div
        prev = div
    total += module

print(total)