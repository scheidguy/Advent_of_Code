
f = open('day4_input.txt')
text = f.readlines()
f.close()

IDsum = 0
for line in text:
    line = line.strip()
    checksum = line[-7:]
    checksum = checksum[1:-1]
    line = line[0:-7]
    ID = int(line[-3:])
    line = line[0:-4]
    letters = line.split('-')
    letters = ''.join(letters)
    counts = [0 for _ in range(26)]
    for letter in letters:
        counts[ord(letter) - 97] += 1
    top5 = ''
    for _ in range(5):
        top5 += chr(97 + counts.index(max(counts)))
        counts[counts.index(max(counts))] = 0
    if top5 == checksum:
        IDsum += ID
    

print(IDsum)
