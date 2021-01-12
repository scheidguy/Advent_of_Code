
f = open('day25-1_input.txt')
# f = open('day25-1_debug.txt')
text = f.readlines()
f.close()


div = 20201227
subj = 7
pkey1 = int(text[0].strip())
pkey2 = int(text[1].strip())
# pkey1 = 5764801
# pkey2 = 17807724

val = 1
loopsize = 0
while True:
    loopsize += 1
    val *= subj
    val = val % div
    if val == pkey1:
        break

val = 1
subj = pkey2
for _ in range(loopsize): 
    val *= subj
    val = val % div
print(val)

