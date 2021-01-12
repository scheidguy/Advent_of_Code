

f = open('day2-1_input.txt')
# f = open('day2-1_debug.txt')
text = f.readlines()
f.close()

program = [int(i) for i in text[0].strip().split(',')]

program[1] = 12
program[2] = 2
pos = 0
while program[pos] != 99:
    first = program[program[pos+1]]
    second = program[program[pos+2]]
    ind = program[pos+3]
    if program[pos] == 1:
        program[ind] = first + second
    elif program[pos] == 2:
        program[ind] = first * second
    else: print('ERROR');break
    pos += 4
    
print(program[0])
