
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
    letters = ' '.join(letters)
    real = ''
    for letter in letters:
        for shift in range(ID):
            if letter == 'z':
                letter = 'a'
            else:
                letter = chr(ord(letter) + 1)
        real += letter
    if 'north' in real: 
        print(real)
        print(ID)
    

    


