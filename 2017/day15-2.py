
prevA = 512
prevB = 191
factorA = 16807
factorB = 48271
div = 2147483647

count = 0
for pairs in range(5000000):
    if pairs % 10**6 == 0: print(pairs)
    prevA = (prevA * factorA) % div
    while prevA % 4 != 0:
        prevA = (prevA * factorA) % div
    prevB = (prevB * factorB) % div
    while prevB % 8 != 0:
        prevB = (prevB * factorB) % div
    binA = bin(prevA)[2:]
    binA = '0'*(16 - len(binA)) + binA[-16:]
    binB = bin(prevB)[2:]
    binB = '0'*(16 - len(binB)) + binB[-16:]
    if binA == binB:
        count += 1

print(count)
