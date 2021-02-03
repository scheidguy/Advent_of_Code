
a = '11011110011011101'
while len(a) < 35651584:
    B = a[::-1]
    b = ''
    for digit in B:
        if digit == '0':
            b += '1'
        else: b += '0'
    a += '0' + b

checksum = a[0:35651584]
while len(checksum) % 2 == 0:
    new = ''
    for i in range(0, len(checksum), 2):
        if checksum[i] == checksum[i+1]:
            new += '1'
        else:
            new += '0'
    checksum = new

print(checksum)
