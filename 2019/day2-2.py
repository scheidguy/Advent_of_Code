
import copy

f = open('day2-1_input.txt')
# f = open('day2-1_debug.txt')
text = f.readlines()
f.close()

program = [int(i) for i in text[0].strip().split(',')]


target = 19690720
P = copy.deepcopy(program)
for noun in range(100):
    for verb in range(100):
        program = copy.deepcopy(P)
        program[1] = noun
        program[2] = verb
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
        if program[0] == target: break
    if program[0] == target: break
    
print(100*noun + verb)
