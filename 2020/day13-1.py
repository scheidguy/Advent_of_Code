

f = open('day13-1_input.txt')
# f = open('day13-1_debug.txt')
text = f.readlines()
f.close()

time = int(text[0])
buses = text[1].split(',')

soon = 10**9
for bus in buses:
    if bus == 'x': continue
    num = int(bus)
    if num - (time % num) < soon:
        soon = num - (time % num)
        thebus = num

print(soon*thebus)



# # [23, 37, 863, 19, 13, 17, 29, 571, 41]

# T = 0
# foundit = False
# while not foundit:
#     if (T / int(maxbus)) % 10**5 == 0: print('PROCESSING...' + str(T))
#     order = maxind - 1
#     for bus in buses:
#         order += 1
#         if bus == maxbus: continue
#         if bus == 'x': continue
#         num = int(bus)
#         ind = B.index[bus]
#         if maxbus-
        
#         if (num - (T % num)) != order: break
#         if bus == buses[-1]: foundit = True
#     T += int(maxbus)
# print(T)
