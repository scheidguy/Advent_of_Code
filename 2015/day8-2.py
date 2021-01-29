
f = open('day8_input.txt')
text = f.readlines()
f.close()

code = 0
encoded = 0
for line in text:
    line = line.strip()
    code += len(line)
    encoded += len(line) + 2
    for i in range(len(line)):
        letter = line[i]
        if letter == '\\': encoded += 1
        if letter == '"': encoded += 1
              
print(encoded - code)
