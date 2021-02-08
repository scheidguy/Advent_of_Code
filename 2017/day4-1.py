
f = open('day4_input.txt')
text = f.readlines()
f.close()

valid = 0
for line in text:
    line = line.strip().split()
    invalid = False
    for word in line:
        if line.count(word) > 1:
            invalid = True
            break
    if not invalid:
        valid += 1

print(valid)
