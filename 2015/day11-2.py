
password = list(map(ord, 'hxbxxyzz'))

valid = False
while not valid:
    password[-1] += 1
    if password[-1] == 123:
        password[-1] = 97
        password[-2] += 1
        if password[-2] == 123:
            password[-2] = 97
            password[-3] += 1
            if password[-3] == 123:
                password[-3] = 97
                password[-4] += 1
                if password[-4] == 123:
                    password[-4] = 97
                    password[-5] += 1
                    if password[-5] == 123:
                        password[-5] = 97
                        password[-6] += 1
    for i in range(len(password)):
        if password[i] == 105 or password[i] == 108 or password[i] == 111:
            password[i] += 1
    straight = False
    for i in range(len(password)-2):
        if password[i+1] - password[i] == 1 and password[i+2] - password[i+1] == 1:
            straight = True
    if not straight:
        continue
    val = 0
    for i in range(len(password)-1):
        if password[i] == password[i+1]:
            if val == 0: val = password[i]
            elif val != password[i]: valid = True;break

print(''.join(list(map(chr, password))))
