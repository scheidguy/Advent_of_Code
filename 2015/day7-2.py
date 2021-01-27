
f = open('day7_input.txt')
# f = open('day7_debug.txt')
text = f.readlines()
f.close()

inputs = {}
for line in text:
    line = line.strip()
    line = line.split(' -> ')
    inputs[line[1]] = line[0].split(' ')

inputs['b'] = ['16076']
while inputs['a'][0].isalpha():
    for key in inputs.keys():
        curr = inputs[key]
        if len(curr) == 1 and curr[0].isnumeric():
            signal = curr[0]
            if int(signal) < 0: signal = str(65536 + int(signal))
            inputs[key] = [signal]
            for key2 in inputs.keys():
                if key in inputs[key2]:
                    for i in range(len(inputs[key2])):
                        if inputs[key2][i] == key:
                            inputs[key2][i] = signal
        if len(curr) == 2 and curr[1].isnumeric():
            signal = str(~ (int(curr[1])))
            if int(signal) < 0: signal = str(65536 + int(signal))
            inputs[key] = [signal]
            for key2 in inputs.keys():
                if key in inputs[key2]:
                    for i in range(len(inputs[key2])):
                        if inputs[key2][i] == key:
                            inputs[key2][i] = signal
        if len(curr) == 3 and curr[0].isnumeric() and curr[2].isnumeric():
            if curr[1] == 'LSHIFT':
                signal = str(int(curr[0]) << int(curr[2]))
            if curr[1] == 'RSHIFT':
                signal = str(int(curr[0]) >> int(curr[2]))
            if curr[1] == 'AND':
                signal = str(int(curr[0]) & int(curr[2]))
            if curr[1] == 'OR':
                signal = str(int(curr[0]) | int(curr[2]))
            if int(signal) < 0: signal = str(65536 + int(signal))
            inputs[key] = [signal]
            for key2 in inputs.keys():
                if key in inputs[key2]:
                    for i in range(len(inputs[key2])):
                        if inputs[key2][i] == key:
                            inputs[key2][i] = signal

print(inputs['a'])
