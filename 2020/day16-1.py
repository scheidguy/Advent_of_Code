
# import copy

f = open('day16-1_input.txt')
# f = open('day16-1_debug.txt')
text = f.readlines()
f.close()

valid = {}
for i in range(20):
    words = text[i].split()
    field = words[0] + ' ' + words[1]
    valid[field] = []
    for word in words:
        if '-' in word:
            limits = [int(i) for i in word.split('-')]
            limits = range(limits[0], limits[1] + 1)
            valid[field].append(limits)

my = [int(i) for i in text[22].split(',')]

error = 0
invalid = []
nearby = text[25:]
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
            
print(error)