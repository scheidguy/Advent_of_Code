
discs = [15, 2, 4, 2, 2, 0]
discmax = [17, 3, 19, 13, 7, 5]
time = 0
target = [16, 1, 16, 9, 2, 4]
while discs != target:
    time += 1
    discs = [(discs[i]+1) % discmax[i] for i in range(6)]
    
print(time)
