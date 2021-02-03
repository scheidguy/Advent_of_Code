
from random import randint
from copy import deepcopy
from time import time


tic = time()
minsteps = 75
for sims in range(1, 10**5):
    if sims % 10**5 == 0:
        print(sims)
    # capital letters are generators, lower case are corresponding microchips
    # seed initial state from day11_input.txt
    floors = [[] for _ in range(4)]
    floors[0] = ['S', 's', 'P', 'p']
    floors[1] = ['T', 'R', 'r', 'C', 'c']
    floors[2] = ['t']
    # floors[0] = ['l', 'h']
    # floors[1] = ['H']
    # floors[2] = ['L']
    elevator = []
    level = 0
    steps = 0
    sequence = []
    while len(floors[3]) != 10:
        steps += 1
        if steps > minsteps:
            break

        if level == 0:
            direction = 'u'
        elif level == 3:
            direction = 'd'
        else:
            if not any([len(floor) for floor in floors[0:level]]):
                direction = 'u'
            else:
                if randint(0, 1):
                    direction = 'u'
                else:
                    direction = 'd'

        ded = True
        attempts = 0
        while ded:
            attempts += 1
            if attempts > 20:
                break
            ded = False
            if len(floors[level]) == 1 or direction == 'd':
                grabbed = 1
            else:
                # grabbed = randint(1, 2)
                grabbed = 2
            pickme = randint(0, len(floors[level])-1)
            grabme = floors[level][pickme]
            floor = deepcopy(floors[level])
            if grabbed == 2:
                pickme2 = randint(0, len(floors[level])-1)
                while pickme == pickme2:
                    pickme2 = randint(0, len(floors[level])-1)
                grabme += floors[level][pickme2]
                floor.pop(max([pickme, pickme2]))
                floor.pop(min([pickme, pickme2]))
            else:
                floor.pop(pickme)
            for item in floor:
                if item.islower() and item.upper() not in floor:
                    for it in floor:
                        if it.isupper():
                            ded = True
            if direction == 'u':
                floor = deepcopy(floors[level+1])
            else:
                floor = deepcopy(floors[level-1])
            for grab in grabme:
                floor.append(grab)
            for item in floor:
                if item.islower() and item.upper() not in floor:
                    for it in floor:
                        if it.isupper():
                            ded = True
        if ded:
            break

        sequence.append(direction + grabme)
        elevator.append(floors[level].pop(floors[level].index(grabme[0])))
        if len(grabme) == 2:
            elevator.append(floors[level].pop(floors[level].index(grabme[1])))
        if direction == 'u':
            level += 1
        if direction == 'd':
            level -= 1
        floors[level].append(elevator.pop())
        if len(grabme) == 2:
            floors[level].append(elevator.pop())
    if not ded and steps < minsteps:
        minsteps = steps
        best = sequence

if minsteps < 75:
    print(minsteps)
print(f'TIME ELAPSED: {round(time() - tic)} seconds')
