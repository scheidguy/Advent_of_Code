
import copy


f = open('day19-2_input.txt')
# f = open('day19-2_debug3.txt')
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
# orders = [['9', '12'], ['124', '57']]
# orders = [['57', '117'], ['12', '73']]
# valid31 = ['bbaba', 'ababb', 'babab', 'bbbaa', 'aabab', 'abaaa', 'abaab', 'baaba', 'babaa', 'aabaa', 'abbba', 'abbaa', 'abbab', 'baaab', 'babba', 'aabba']
valid31 = ['bbbabbbb', 'aabbbaaa', 'babbaaab', 'bbabbaaa', 'bbbbbbbb', 'bbbabaaa', 'bbbaaabb', 'bbbabbab', 'bbbababb', 'abbbbbbb', 'abbaabaa', 'aaabbaaa', 'aababaaa', 'aabbbaba', 'aabbaaaa', 'baabbaba', 'babaaaab', 'babbbbba', 'babbabba', 'bbaaabab', 'bbabaaab', 'bbabbbab', 'bbbbabba', 'bbbbbaaa', 'bbbababa', 'aaaaabab', 'aaaababb', 'abaababb', 'abbaabbb', 'abbbabbb', 'abbbbabb', 'abaaabba', 'abbbbaaa', 'abbabbaa', 'abbaabba', 'aaaabbaa', 'aaabaaaa', 'aaabbbba', 'aabababa', 'aabbabba', 'aabbaaba', 'baaababa', 'baabaabb', 'baabaaaa', 'baababba', 'baabaaba', 'bababbab', 'babaabba', 'babbbabb', 'babbaaaa', 'babbabaa', 'bbaabaaa', 'bbaababb', 'bbaabbab', 'bbababaa', 'bbabbaab', 'bbbbaaba', 'bbbbabbb', 'bbbbbbba', 'bbbaabba', 'bbbaaaba', 'abbabaab', 'abbbbbab', 'abababab', 'aabbabbb', 'aabbaabb', 'aabbbabb', 'ababbabb', 'abaaabbb', 'abaaaabb', 'abbaaabb', 'abbbaabb', 'ababbbaa', 'ababaaba', 'abaababa', 'abbbbaba', 'abbababa', 'abbabaaa', 'aaaaabba', 'aaaabaaa', 'aaababba', 'aabaabba', 'aabaaaba', 'baaababb', 'baaaabaa', 'baaaabba', 'baaaaaba', 'baabbabb', 'baababbb', 'bababbbb', 'babaaaaa', 'babaabaa', 'babbbaba', 'babbbaab', 'bbaababa', 'bbaaaaaa', 'bbaaaabb', 'bbababbb', 'bbbbaaaa', 'aabbbaab', 'aaabbbab', 'abbabbab', 'ababbbab', 'aaababab', 'aaabbbbb', 'aaaaaabb', 'aabaaabb', 'ababaabb', 'abaaaaaa', 'ababaaaa', 'ababbaaa', 'ababbbba', 'abbbaaba', 'aaaaabaa', 'aaaaaaba', 'baaabaab', 'baaaaabb', 'baaabaaa', 'aaabbaab', 'aababaab', 'aabbaaab', 'aaababbb', 'aaaabbbb', 'abaabbaa', 'baaabbab', 'aaabaaab', 'aaaabaab', 'aabaaaab']
valid42 = ['abbaaaaa', 'baabbaab', 'bbabbbba', 'abaaaaba', 'aabbbbaa', 'abbbabaa', 'abaabaaa', 'abbbaaaa', 'bbaabbbb', 'bbbbabab', 'abbaaaab', 'bbbabaab', 'ababbaab', 'bbbbbaab', 'babababa', 'bbbbbbaa', 'bbaaabaa', 'bbabbaba', 'bbaabbba', 'bbababba', 'abababba', 'aaaababa', 'aaabaaba', 'abbaaaba', 'aaababaa', 'aabaaaaa', 'aababbaa', 'aabbabaa', 'abababaa', 'abbbbbaa', 'aaabaabb', 'aabaabbb', 'aababbbb', 'bbabbbbb', 'baaabbbb', 'aabbbbab', 'baabbbab', 'bbbbbbab', 'bbbaabab', 'bbababab', 'baabaaab', 'bbaaaaab', 'bbbaaaab', 'abaabaab', 'bbaabaab', 'bababaab', 'abbbbaab', 'bababbaa', 'baaabbba', 'babaaaba', 'bbbbbaba', 'bbbaaaaa', 'bbbabbaa', 'bbbbabaa', 'bbabaaaa', 'bbaabbaa', 'bbaaaaba', 'bbabaaba', 'bbaaabba', 'aabbbbba', 'abbbabba', 'ababbaba', 'aaaaaaaa', 'aaabbbaa', 'aabaabaa', 'abaaabaa', 'bbbbbabb', 'babaaabb', 'bbbaabbb', 'abababbb', 'aaaaabbb', 'abbabbbb', 'aabbbbbb', 'babbbbbb', 'baabbbbb', 'aabaabab', 'abaabbab', 'aaaabbab', 'aababbab', 'babbabab', 'babbbbab', 'ababaaab', 'bbbbaaab', 'abaaaaab', 'baaaaaab', 'baaaaaaa', 'baabbbaa', 'babbbbaa', 'bababbba', 'baabbbba', 'babbaaba', 'bbbabbba', 'bbbaabaa', 'bbabbbaa', 'abbabbba', 'abbbbbba', 'aaabbaba', 'aabababb', 'aaabbabb', 'bbabaabb', 'babbaabb', 'babbabbb', 'bbaaabbb', 'ababbbbb', 'abaabbbb', 'abbbabab', 'aabbabab', 'baababab', 'babaabab', 'abbbaaab', 'aaaaaaab', 'babbbaaa', 'baababaa', 'baaabbaa', 'aababbba', 'abaabbba', 'babababb', 'abbababb', 'bbabbabb', 'bbbbaabb', 'baaaabbb', 'babaabbb', 'abaaabab', 'abbaabab', 'baaaabab', 'bababaaa', 'baabbaaa', 'aaaabbba']
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
chunk = 8
for message in messages:
    m = message.strip()
    if len(m) == 3*chunk:
        if m[0:chunk] in valid42 and m[chunk:2*chunk] in valid42 and m[2*chunk:3*chunk] in valid31:
            matches += 1
    else:
        good2go = False
        max31s = ((len(m) // chunk) - 1) // 2  # minus one accounts for min of 1 rule 8=[42]
        for num31 in range(1, max31s + 1):
            good42 = True
            good31 = True
            mess42 = m[0:-chunk*num31]
            mess31 = m[-chunk*num31:]
            for _ in range(len(mess31) // chunk):
                m31 = mess31[0:chunk]
                if len(mess31) != len(m31): mess31 = mess31[chunk:]
                if m31 not in valid31: good31 = False;break
            if not good31: continue
            for _ in range(len(mess42) // chunk):
                m42 = mess42[0:chunk]
                if len(mess42) != len(m42): mess42 = mess42[chunk:]
                if m42 not in valid42: good42 = False;break
            if good42 and good31: good2go = True;break

        if good2go: matches += 1
print(matches)
