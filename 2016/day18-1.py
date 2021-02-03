
f = open('day18_input.txt')
text = f.readlines()
f.close()


for line in text:
    line = line.strip()
    
line = '.' + line + '.'

rows = [line]
safes = line.count('.') - 2
for row in range(39):
    newrow = ['.' for _ in range(len(line))]
    prevrow = rows[-1]
    for tile in range(1, len(line) - 1):
        lcr = prevrow[tile-1:tile+2]
        if lcr == '^^.' or lcr == '.^^' or lcr == '^..' or lcr == '..^':
            newrow[tile] = '^'
    rows.append(''.join(newrow))
    safes += rows[-1].count('.') - 2

print(safes)
