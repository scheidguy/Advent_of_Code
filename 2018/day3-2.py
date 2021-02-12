
import numpy as np


f = open('day3_input.txt')
text = f.readlines()
f.close()

fabric = np.zeros((1000, 1000), dtype=int)
for line in text:
    line = line.strip().split()
    ID = int(line[0][1:])
    margins = line[2].strip(':').split(',')
    dims = line[3].split('x')
    margin0 = int(margins[0])
    margin1 = int(margins[1])
    dim0 = int(dims[0])
    dim1 = int(dims[1])

    fabric[margin0:margin0+dim0, margin1:margin1+dim1] += 1
    
for line in text:
    line = line.strip().split()
    ID = int(line[0][1:])
    margins = line[2].strip(':').split(',')
    dims = line[3].split('x')
    margin0 = int(margins[0])
    margin1 = int(margins[1])
    dim0 = int(dims[0])
    dim1 = int(dims[1])

    if len(np.where(fabric[margin0:margin0+dim0, margin1:margin1+dim1] > 1)[0]) == 0:
        print(ID)
