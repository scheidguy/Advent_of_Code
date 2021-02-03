
import hashlib


def possiblepaths(row, col, passcode):
    global MAXLENGTH
    if row == 3 and col == 3:
        if len(passcode) - 8 > MAXLENGTH:
            MAXLENGTH = len(passcode) - 8
        return
    result = hashlib.md5(passcode.encode())
    thehash = result.hexdigest()
    doors = ''
    if thehash[0] in 'bcdef':
        if row != 0:
            doors += 'U'
    if thehash[1] in 'bcdef':
        if row != 3:
            doors += 'D'
    if thehash[2] in 'bcdef':
        if col != 0:
            doors += 'L'
    if thehash[3] in 'bcdef':
        if col != 3:
            doors += 'R'
    if len(doors) == 0:
        return
    for door in doors:
        if door == 'U':
            possiblepaths(row - 1, col, passcode + door)
        if door == 'D':
            possiblepaths(row + 1, col, passcode + door)
        if door == 'L':
            possiblepaths(row, col - 1, passcode + door)
        if door == 'R':
            possiblepaths(row, col + 1, passcode + door)


MAXLENGTH = 0
passcode = 'vkjiggvb'
possiblepaths(0, 0, passcode)
print(MAXLENGTH)
