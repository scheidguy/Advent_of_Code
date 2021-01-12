
# import copy

# f = open('day16-1_input.txt')
f = open('day16-1_debug.txt')
text = f.readlines()
f.close()

valid = {}
for i in range(3):
    words = text[i].split()
    field = words[0] + ' ' + words[1]
    valid[field] = []
    for word in words:
        if '-' in word:
            limits = [int(i) for i in word.split('-')]
            limits = range(limits[0], limits[1] + 1)
            valid[field].append(limits)

my = [int(i) for i in text[5].split(',')]

error = 0
invalid = []
nearby = text[8:]
row = -1
for tick in nearby:
    row += 1
    tick = [int(i) for i in tick.split(',')]
    # valid2 = copy.deepcopy(valid)
    for num in tick:
        good2go = False
        for k in valid.keys():
            entry = valid[k]
            if num in entry[0] or num in entry[1]: good2go = True
        if not good2go:
            error += num
            if row not in invalid: invalid.append(row)

for r in invalid[::-1]: nearby.pop(r)


for ind in range(len(nearby)):
    nearby[ind] = [int(i) for i in nearby[ind].split(',')]
nearby.append([int(i) for i in text[5].split(',')])


found = []
prod = 1
while len(found) < 3:
    for fie in valid.keys():
        if fie == 'arrival track:':
            print('stop')
        entry = valid[fie]
        good2go = True
        cols = list(range(3))
        for col in cols:
            for tick in nearby:
                if col == -1 or col in found: break
                if tick[col] not in entry[0] and tick[col] not in entry[1]:
                    cols[col] = -1
                    break
        cols.sort()
        for i in found: cols.remove(i)
        if len(cols) == 1: found.append(cols[-1]);break
        if cols[-2] == -1:
            if cols[-1] == -1:
                print('wut')
            if fie[0:9] == 'departure': prod *= cols[-1]
            found.append(cols[-1])
            
            print(fie + 'column: ' + str(cols[-1]))
            
        

print(prod)
        
    



