
f = open('day2_input.txt')
text = f.readlines()
f.close()

keypad = [[1,2,3], [4,5,6], [7,8,9]]
row = col = 1
code = ''
for line in text:
    line = line.strip()
    for letter in line:
        if letter == 'U':
            if row != 0: row -= 1
        if letter == 'D':
            if row != 2: row += 1
        if letter == 'R':
            if col != 2: col += 1
        if letter == 'L':
            if col != 0: col -= 1
    code += str(keypad[row][col])

print(code)
