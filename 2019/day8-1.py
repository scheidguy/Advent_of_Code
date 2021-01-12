

f = open('day8-1_input.txt')
# f = open('day8-1_debug.txt')
text = f.readlines()
f.close()

digits = text[0].strip()
width = 25
height = 6

numzeros = []
ind = 0
for layer in range(len(digits)//width//height):
    numzeros.append(digits[ind:ind+width*height].count('0'))
    ind += width*height

minlayer = numzeros.index(min(numzeros))
num1 = digits[minlayer*width*height:(minlayer+1)*width*height].count('1')
num2 = digits[minlayer*width*height:(minlayer+1)*width*height].count('2')

print(num1*num2)
