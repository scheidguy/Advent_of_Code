

f = open('day5_input.txt')
text = f.readlines()
f.close()

nice = 0
for line in text:
    line = line.strip()
    num = 0
    ind = 0
    sandwich = False
    double = False
    prev = ''
    for letter in line:
        if ind > 1: prev = line[ind-2]
        if letter == prev: sandwich = True
        if ind > 0 and ind != len(line)-1:
            if line[ind-1:ind+1] in line[ind+1:]: double = True
        ind += 1
    if double and sandwich: nice += 1
    
print(nice)
