
import numpy as np


f = open('day13_input.txt')
text = f.readlines()
f.close()

track = []
rows = []
cols = []
orients = []
row = -1
for line in text:
    row += 1
    line = line.strip('/n')
    track.append(list(line))
    col = -1
    for letter in line:
        col += 1
        if letter in 'v<>^':
            cols.append(col)
            rows.append(row)
            orients.append(letter)

track[-1].append(' ')
track = np.array(track)
for i in range(len(rows)):
    if orients[i] in '<>':
        track[rows[i], cols[i]] = '-'
    else:
        track[rows[i], cols[i]] = '|'
turns = ['L' for cart in range(len(rows))]
order = [1000*rows[i] + cols[i] for i in range(len(rows))]
scores = [1000*rows[i] + cols[i] for i in range(len(rows))]
ticks = 0
nocrash = True
while len(rows) > 0 and nocrash:
    ticks += 1
    for _ in range(len(rows)):
        i = order.index(min(order))
        order[i] = 10**6
        row = rows[i]
        col = cols[i]
        if orients[i] == '^':
            row -= 1
            if track[row, col] == '+':
                if turns[i] == 'L':
                    turns[i] = 'S'
                    orients[i] = '<'
                elif turns[i] == 'S':
                    turns[i] = 'R'
                elif turns[i] == 'R':
                    turns[i] = 'L'
                    orients[i] = '>'
            elif track[row, col] == 'f':
                orients[i] = '>'
            elif track[row, col] == 'b':
                orients[i] = '<'
        elif orients[i] == 'v':
            row += 1
            if track[row, col] == '+':
                if turns[i] == 'L':
                    turns[i] = 'S'
                    orients[i] = '>'
                elif turns[i] == 'S':
                    turns[i] = 'R'
                elif turns[i] == 'R':
                    turns[i] = 'L'
                    orients[i] = '<'
            elif track[row, col] == 'f':
                orients[i] = '<'
            elif track[row, col] == 'b':
                orients[i] = '>'
        elif orients[i] == '>':
            col += 1
            if track[row, col] == '+':
                if turns[i] == 'L':
                    turns[i] = 'S'
                    orients[i] = '^'
                elif turns[i] == 'S':
                    turns[i] = 'R'
                elif turns[i] == 'R':
                    turns[i] = 'L'
                    orients[i] = 'v'
            elif track[row, col] == 'f':
                orients[i] = '^'
            elif track[row, col] == 'b':
                orients[i] = 'v'
        elif orients[i] == '<':
            col -= 1
            if track[row, col] == '+':
                if turns[i] == 'L':
                    turns[i] = 'S'
                    orients[i] = 'v'
                elif turns[i] == 'S':
                    turns[i] = 'R'
                elif turns[i] == 'R':
                    turns[i] = 'L'
                    orients[i] = '^'
            elif track[row, col] == 'f':
                orients[i] = 'v'
            elif track[row, col] == 'b':
                orients[i] = '^'
        
        rows[i] = row
        cols[i] = col
        scores[i] = 1000*row + col
        for j in range(len(scores)):
            if i == j: continue
            if scores[i] == scores[j]:
                track[row, col] = 'X'
                nocrash = False
        if not nocrash: break
    
    order = [1000*rows[i] + cols[i] for i in range(len(rows))]

print(col, row)
