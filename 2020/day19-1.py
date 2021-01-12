
import copy


f = open('day19-1_input.txt')
# f = open('day19-1_debug.txt')
text = f.readlines()
f.close()

rules = {}
for row in range(len(text)):
    if text[row] == '\n': row += 1;break
    line = text[row].split(':')
    rulenum = line[0]
    rule = line[1].split('|')
    rules[rulenum] = [r.split() for r in rule]

rules['12'] = 'a'
rules['57'] = 'b'
orders = [['8', '11']]
valid = []
iterations = 0
while len(orders) > 0:
    iterations += 1
    if iterations % 100000 == 0: print(iterations)
    order = orders[0]
    while '12' in order: order[order.index('12')] = 'a'
    while '57' in order: order[order.index('57')] = 'b'
    string = ''
    if string.join(order).isalpha():
        valid.append(string.join(orders.pop(0)))
        continue
    subind = 0
    while order[subind].isalpha(): subind += 1
    rule = order.pop(subind)
    branches = 0
    for branch in rules[rule]:
        branch = copy.deepcopy(branch)
        branches += 1
        branchlength = len(branch)
        if branches == 2:
            orders.append(order)
        while len(branch) > 0: order.insert(subind, branch.pop())
        order = copy.deepcopy(order)
        for _ in range(branchlength): order.pop(subind)

messages = text[row:]
matches = 0
curr = '0'
for message in messages:
    message = message.strip()
    if message in valid: matches += 1
    
print(matches)
