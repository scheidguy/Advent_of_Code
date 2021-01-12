

f = open('day8-1_input.txt')
# f = open('day8-1_debug.txt')
text = f.readlines()
f.close()

digits = text[0].strip()
width = 25
height = 6

message = [['_' for _ in range(width)] for __ in range(height)]
ind = 0
for layer in range(len(digits)//width//height):
    curr = digits[layer*width*height:(layer+1)*width*height]
    for row in range(height):
        for col in range(width):
            if message[row][col] == '_':
                if curr[row*width + col] == '0': message[row][col] = ' '
                if curr[row*width + col] == '1': message[row][col] = 'X'


for row in range(height): print(''.join(message[row]))
