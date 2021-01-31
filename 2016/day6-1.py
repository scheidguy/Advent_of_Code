
f = open('day6_input.txt')
text = f.readlines()
f.close()

counts = [[0 for _ in range(26)] for __ in range(8)]
for line in text:
    line = line.strip()
    ind = -1
    for letter in line:
        ind += 1
        counts[ind][ord(letter) - 97] += 1

password = ''
for i in range(8):
    password += str(chr(97 + counts[i].index(max(counts[i]))))

print(password)
