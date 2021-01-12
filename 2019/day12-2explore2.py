
# import numpy as np


# MY INPUT:
# <x=-15, y=1, z=4>
# <x=1, y=-10, z=-8>
# <x=-5, y=4, z=9>
# <x=4, y=6, z=-2>
moonspos = [[-15,1,4], [1,-10,-8], [-5,4,9], [4,6,-2]]

# DEBUG:
# <x=-1, y=0, z=2>
# <x=2, y=-10, z=-7>
# <x=4, y=-8, z=8>
# <x=3, y=5, z=-1>
moonspos = [[-1,0,2], [2,-10,-7], [4,-8,8], [3,5,-1]]

# DEBUG2:
# <x=-8, y=-10, z=0>
# <x=5, y=5, z=10>
# <x=2, y=-7, z=3>
# <x=9, y=-8, z=-3>
# moonspos = [[-8,-10,0], [5,5,10], [2,-7,3], [9,-8,-3]]

moonsvel = [[0,0,0] for _ in range(len(moonspos))]
# s1 = {}
# s1[' '.join(map(str, moonspos[0]))] = set()
# s1[' '.join(map(str, moonspos[0]))].add(tuple(moonsvel[0]))
# s2 = {}
# s2[' '.join(map(str, moonspos[1]))] = set()
# s2[' '.join(map(str, moonspos[1]))].add(tuple(moonsvel[1]))
# s3 = {}
# s3[' '.join(map(str, moonspos[2]))] = set()
# s3[' '.join(map(str, moonspos[2]))].add(tuple(moonsvel[2]))
# s4 = {}
# s4[' '.join(map(str, moonspos[3]))] = set()
# s4[' '.join(map(str, moonspos[3S]))].add(tuple(moonsvel[3]))
# states = [s1, s2, s3, s4]

state = ''
checksum = 0
for i in range(len(moonspos)):
    state += ' '.join(map(str, moonspos[i]))
    state += ' ' + ' '.join(map(str, moonsvel[i])) + ' '
    checksum += sum(moonspos[i]) * sum(moonsvel[i])

seen = {}
seen[checksum] = set()
seen[checksum].add(state)
timesteps = 0
while True:
    timesteps += 1
    if timesteps % 10**6 == 0: print(timesteps)
    for m1 in range(len(moonspos)):
        for m2 in range(m1 + 1, len(moonspos)):
            for c in range(len(moonspos[0])):
                if moonspos[m1][c] > moonspos[m2][c]:
                    moonsvel[m1][c] -= 1
                    moonsvel[m2][c] += 1
                elif moonspos[m1][c] < moonspos[m2][c]:
                    moonsvel[m1][c] += 1
                    moonsvel[m2][c] -= 1

    # matches = 0
    for m in range(len(moonspos)):
        moonspos[m][0] += moonsvel[m][0]
        moonspos[m][1] += moonsvel[m][1]
        moonspos[m][2] += moonsvel[m][2]
        # key = ' '.join(map(str, moonspos[m]))
        # vel = tuple(moonsvel[m])
        # if key not in states[m].keys():
        #     states[m][key] = set()
        #     states[m][key].add(vel)
        # elif vel not in states[m][key]:
        #     states[m][key].add(vel)
        # else:
        #     matches += 1
    # if matches == len(moonspos):
    state = ''
    checksum = 0
    for i in range(len(moonspos)):
        state += ' '.join(map(str, moonspos[i]))
        state += ' ' + ' '.join(map(str, moonsvel[i])) + ' '
        checksum += sum(moonspos[i]) * sum(moonsvel[i])
    if checksum not in seen.keys():
        seen[checksum] = set()
        seen[checksum].add(state)
    elif state not in seen[checksum]:
        seen[checksum].add(state)
    else:
        print(timesteps)
        break
    # if timesteps == 1000: break

# energy = 0
# for moon in range(len(moonspos)):
#     pot=abs(moonspos[moon][0])+abs(moonspos[moon][1])+abs(moonspos[moon][2])
#     kin=abs(moonsvel[moon][0])+abs(moonsvel[moon][1])+abs(moonsvel[moon][2])
#     energy += pot * kin
# print(energy)
