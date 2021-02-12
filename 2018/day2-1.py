
f = open('day2_input.txt')
text = f.readlines()
f.close()

twos = 0
threes = 0
for line in text:
    line = line.strip()
    line = list(line)
    flag2 = False
    flag3 = False
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        if line.count(letter) == 2:
            flag2 = True
        if line.count(letter) == 3:
            flag3 = True
    if flag2:
        twos += 1
    if flag3:
        threes += 1
print(twos * threes)
