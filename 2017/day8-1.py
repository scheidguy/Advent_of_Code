
f = open('day8_input.txt')
text = f.readlines()
f.close()

registers = {}
for line in text:
    line = line.strip().split()
    registers[line[0]] = 0
for line in text:
    line = line.strip().split()
    register = line[-3]
    if eval(str(registers[register])  + line[-2] + line[-1]):
        if line[1] == 'inc':
            registers[line[0]] += int(line[2])
        else:
            registers[line[0]] -= int(line[2])

print(max(registers.values()))
