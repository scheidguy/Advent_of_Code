
import hashlib


# salt = 'ngcjuoqr'
salt = 'abc'


keys = 0
num = -1
alldone = False
while not alldone:
    num += 1
    three = False
    inp = salt + str(num)
    result = hashlib.md5(inp.encode())
    thehash = result.hexdigest()
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
            inp2 = salt + str(n)
            result2 = hashlib.md5(inp2.encode())
            thehash2 = result2.hexdigest()
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
                        # print(f'Key {keys}:\t{num}\t{n}\t{n-num}\t{triplet}\t{digit1}\t{thehash}\t{thehash2}')
                        if keys == 64:
                            alldone = True
                            print(num)
                        break
                if iskey: break
            if iskey or alldone: break
        