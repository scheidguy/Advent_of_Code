

f = open('day2_input.txt')
text = f.readlines()
f.close()

ribbon = 0
for line in text:
    line = line.strip()
    dims = line.split('x')
    dims = list(map(int, dims))
    ribbon += dims[0] * dims[1] * dims[2]
    maxdim = max(dims)
    dims.pop(dims.index(maxdim))
    ribbon += 2 * (dims[0] + dims[1])
    
print(ribbon)
