
import hashlib


door = 'ugkcyxxp'

password = ['' for _ in range(8)]
num = -1
while password.count('') > 0:
    num += 1
    inp = door + str(num)
    result = hashlib.md5(inp.encode())
    thehash = result.hexdigest()
    if thehash[0:5] == '00000':
        if thehash[5] in '01234567':
            pos = int(thehash[5])
            if password[pos] == '':
                password[pos] = thehash[6]
                print(password[pos])

print(''.join(password))
