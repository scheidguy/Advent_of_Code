

f = open('day2_input.txt')
text = f.readlines()
f.close()

area = 0
for line in text:
    line = line.strip()
    dims = line.split('x')
    dims = list(map(int, dims))
    length = dims[0]
    width = dims[1]
    height = dims[2]
    area += 2 * (length*width + length*height + width*height)
    maxdim = max(dims)
    dims.pop(dims.index(maxdim))
    area += dims[0] * dims[1]
print(area)
