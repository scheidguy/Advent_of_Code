
import hashlib


inp = 'iwrupvqb'

num = 0
while True:
    num += 1
    newinp = inp + str(num)
    out = hashlib.md5(newinp.encode('utf-8')).hexdigest()
    if out[0:5] == '00000': break
print(num)
