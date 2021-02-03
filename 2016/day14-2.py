
import hashlib


# salt = 'ngcjuoqr'
salt = 'abc'

keys = 0
num = -1
alldone = False
hashes = []
while not alldone:
    num += 1
    three = False
    if num >= len(hashes):
        thehash = salt + str(num)
        for _ in range(2017):
            result = hashlib.md5(thehash.encode())
            thehash = result.hexdigest()
        hashes.append(thehash)
    thehash = hashes[num]
    for i in range(len(thehash) - 2):
        digit1 = thehash[i]
        digit2 = thehash[i+1]
        digit3 = thehash[i+2]
        if digit1 == digit2 and digit1 == digit3:
            three = True
            triplet = digit1
            break
    if three:
        iskey = False
        for n in range(num + 1, num + 1001):
            if n >= len(hashes):
                thehash2 = salt + str(n)
                for _ in range(2017):
                    result = hashlib.md5(thehash2.encode())
                    thehash2 = result.hexdigest()
                hashes.append(thehash2)
            thehash2 = hashes[n]
            for i in range(len(thehash2) - 4):
                digit1 = thehash2[i]
                digit2 = thehash2[i+1]
                digit3 = thehash2[i+2]
                digit4 = thehash2[i+3]
                digit5 = thehash2[i+4]
                if digit1 == digit2 and digit1 == digit3 and digit1 == digit4 and digit1 == digit5:
                    if triplet == digit1:
                        keys += 1
                        iskey = True
                        print(keys)
                        if keys == 64:
                            alldone = True
                            print(num)
                        break
                if iskey: break
            if iskey or alldone: break
        