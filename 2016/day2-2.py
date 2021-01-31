
f = open('day2_input.txt')
text = f.readlines()
f.close()

keypad = [['0','0','1','0','0'], ['0','2','3','4','0'], ['5','6','7','8','9'], ['0','A','B','C','0'], ['0','0','D','0','0']]
row = 2
col = 0
code = ''
for line in text:
    line = line.strip()
    for letter in line:
        if letter == 'U':
            if row == 1 and col == 2: row -= 1
            elif row == 2 and col in range(1,4): row -= 1
            elif row == 4 or row == 3: row -= 1
        if letter == 'D':
            if row == 3 and col == 2: row += 1
            elif row == 2 and col in range(1,4): row += 1
            elif row == 0 or row == 1: row += 1
        if letter == 'R':
            # if row == 1 and col == 2: col += 1
            if col == 2 and row in range(1,4): col += 1
            elif col == 3 and row == 2: col += 1
            elif col == 0 or col == 1: col += 1
        if letter == 'L':
            if col == 2 and row in range(1,4): col -= 1
            elif col == 1 and row == 2: col -= 1
            elif col == 4 or col == 3: col -= 1
    code += keypad[row][col]

print(code)
