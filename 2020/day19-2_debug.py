
import copy


# f = open('day19-2_input.txt')
f = open('day19-2_debug2.txt')
text = f.readlines()
f.close()

rules = {}
for row in range(len(text)):
    if text[row] == '\n': row += 1;break
    line = text[row].split(':')
    rulenum = line[0]
    rule = line[1].split('|')
    rules[rulenum] = [r.split() for r in rule]
    
# i=1
# for i in range(2,2):
#     rules[str(100*i)] = [['42', '31'], ['42', str(100*(i+1)), '31']]
# rules[str(100*(i+1))] = [['42', '31']]

# for i in range(2,2):
#     rules[str(101*i)] = [['42'], ['42', str(101*(i+1))]]
# rules[str(101*(i+1))] = [['42']]
# rules['8'] = [['42']]
# rules['11'] = [['42', '31']]
# rules['200'] = [['42', '31']]
# rules['202'] = [['42']]

rules['1'] = 'a'
rules['14'] = 'b'
orders = [['8', '11']]
valid = []
iterations = 0
while len(orders) > 0:
    iterations += 1
    if iterations % 100000 == 0: print(iterations)
    order = orders[0]
    while '1' in order: order[order.index('1')] = 'a'
    while '14' in order: order[order.index('14')] = 'b'
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
