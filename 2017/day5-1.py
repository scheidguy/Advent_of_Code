
f = open('day5_input.txt')
text = f.readlines()
f.close()

steps = 0
pos = 0
program = [int(line.strip()) for line in text]
while True:
    steps += 1
    program[pos] += 1
    pos += program[pos] - 1
    if pos not in range(len(program)):
        break

print(steps)
