
f = open('day8_input.txt')
text = f.readlines()
f.close()

code = 0
memory = 0
for line in text:
    line = line.strip()
    code += len(line)
    memory += len(bytes(line[1:-1], "utf-8").decode("unicode_escape"))            

print(code - memory)
