
import hashlib


door = 'ugkcyxxp'

password = ''
num = -1
while len(password) < 8:
    num += 1
    inp = door + str(num)
    result = hashlib.md5(inp.encode())
    thehash = result.hexdigest()
    if thehash[0:5] == '00000':
        password += thehash[5]
        print(password)

print(password)
