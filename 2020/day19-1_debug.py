
import copy


# f = open('day19-1_input.txt')
f = open('day19-1_debug.txt')
text = f.readlines()
f.close()

rules = {}
for row in range(len(text)):
    if text[row] == '\n': row += 1;break
    line = text[row].split(':')
    rulenum = line[0]
    rule = line[1].split('|')
    rules[rulenum] = [r.split() for r in rule]

rules['4'] = 'a'
rules['5'] = 'b'
orders = [['4', '1', '5']]
valid = []
while len(orders) > 0:
    for ind in range(len(orders)):
        order = orders[ind]
        while '4' in order: order[order.index('4')] = 'a'
        while '5' in order: order[order.index('5')] = 'b'
        string = ''
        if string.join(order).isalpha():
            valid.append(string.join(orders.pop(ind)))
            break
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
                # while len(branch) > 0: orders[-1].insert(subind, branch.pop())
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



# curr = '-1'
# alph = ['12', '57']
# while rules['0'][0][0] == '8' or  rules['0'][0][0] == '11':
#     for parsed in alph:
#         for key in rules.keys():
#             if type(rules[key]) == list:
#                 for branch in rule:
#                     for order in branch:
#                         if order in alph:
#                             rules
