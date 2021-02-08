
f = open('day2_input.txt')
text = f.readlines()
f.close()

checksum = 0
for line in text:
    line = line.strip().split()
    line = list(map(int, line))
    checksum += max(line) - min(line)
    
print(checksum)
