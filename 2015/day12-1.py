
f = open('day12_input.txt')
text = f.readlines()
f.close()

num = 0
for line in text:
    line = line.strip()
    n = ''
    for i in range(len(line)):
        if line[i].isnumeric():
            if line[i-1] == '-': n += '-'
            n += line[i]
        else:
            if len(n) > 0: 
                num += int(n)
            n = ''
   
print(num)
