
f = open('day2_input.txt')
text = f.readlines()
f.close()

checksum = 0
for line in text:
    line = line.strip().split()
    line = list(map(int, line))
    alldone = False
    for num1 in line:
        if alldone: break
        for num2 in line:
            if num1 % num2 == 0 and num1 != num2:
                checksum += num1 // num2
                alldone = True
                break
    
print(checksum)
