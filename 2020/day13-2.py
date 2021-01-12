

f = open('day13-1_input.txt')
# f = open('day13-1_debug.txt')
text = f.readlines()
f.close()

buses = text[1].split(',')
# buses = ['1789','37','47','1889']
B = [int(i) for i in buses if i.isnumeric()]
Binds = [buses.index(i) for i in buses if i.isnumeric()]
maxind = buses.index(str(max(B)))
maxbus = buses[maxind]
# [23, 37, 863, 19, 13, 17, 29, 571, 41]

T = 10457834
foundit = False
while not foundit:
    if (T / int(maxbus)) % 10**6 == 0: print('PROCESSING...' + str(T))
    order = maxind - 1
    for bus in buses:
        order += 1
        if bus == maxbus:
            if bus == buses[-1]: foundit = True
            continue
        if bus == 'x': continue
        num = int(bus)
        ind = Binds[B.index(num)]
        if (T-maxind+ind) % num != 0: break
        # if T > 10**8: exit()
        # else: print(T)
        if bus == buses[-1]: foundit = True
    T += int(maxbus) * 571 * 37
print(T-int(maxbus)-maxind)



# soon = 10**9
# minute = 0
# for bus in buses:
#     if bus == 'x': continue
#     num = int(bus)
#     if num - (time % num) < soon:
#         soon = num - (time % num)
#         thebus = num

# print(soon*thebus)
