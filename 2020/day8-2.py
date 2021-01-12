

f = open('day8-1_input.txt')
text = f.readlines()
f.close()

ind = -1
for l in text:
    ind += 1
    l = l.split()
    if l[0] == 'jmp': switch = True
    elif l[0] == 'nop': switch = True
    else: switch = False
    

    row = 0
    rows = [0]
    accum = 0
    while True:
        line = text[row]
        command = line.split()[0]
        val = int(line.split()[1])
            
        if command == 'acc':
            accum += val
            row += 1
            rows.append(row)
            
        elif command == 'nop':
            if switch and row == ind:
                row += val
                rows.append(row)
            else:
                row += 1
                rows.append(row)
            
        elif command == 'jmp':
            if switch and row == ind:
                row += 1
                rows.append(row)
            else:
                row += val
                rows.append(row)
                
        if rows.count(row) == 2: break
        if row == len(text):
            print(accum)
            break
        
        
# # Depth First Search:
# # PARENTS is dictionary showing parents of each bag
# from collections import deque
# SEEN = set()
# Q = deque(['shiny gold'])
# while Q:  # keep investigating until have SEEN all possible
#     x = Q.popleft()
#     if x in SEEN: continue
#     SEEN.add(x)
#     for y in PARENTS[x]: Q.append(y)
# print(len(SEEN) - 1)  # This is all ancestors of shiny gold


# # Recursive function to find number of bags within shiny gold
# def size(bag):
#     ans = 1  # The bag itself
#     for (n, y) in CONTENTS[bag]:
#         ans += n * size(y)  # recurse until reaching a terminal bag
#     return ans
# print(size('shiny gold') - 1)  # subtract 1 b/c don't want to count itself























    
    