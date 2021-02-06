

for num in range(10**8):
    if num % 10**7 == 0: print(num)
    d = 2534 + num
    a = d
    clock = []
    if d % 2 == 0:
        clock.append(0)
    else: continue

    good2go = True
    while a > 0:
        a = a // 2
        if a % 2 == 0 and clock[-1] == 1:
            clock.append(0)
        elif a % 2 == 1 and clock[-1] == 0:
            clock.append(1)
        else:
            good2go = False
            break
    if good2go: # and len(clock) % 2 == 0:
        break
        
    
    