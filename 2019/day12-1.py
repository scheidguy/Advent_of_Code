
# MY INPUT:
# <x=-15, y=1, z=4>
# <x=1, y=-10, z=-8>
# <x=-5, y=4, z=9>
# <x=4, y=6, z=-2>
    
moonspos = [[-15,1,4], [1,-10,-8], [-5,4,9], [4,6,-2]]
moonsvel = [[0,0,0] for _ in range(len(moonspos))]

for t in range(1000):
    for m1 in range(len(moonspos)):
        for m2 in range(m1 + 1, len(moonspos)):
            for c in range(len(moonspos[0])):
                if moonspos[m1][c] > moonspos[m2][c]:
                    moonsvel[m1][c] -= 1
                    moonsvel[m2][c] += 1
                elif moonspos[m1][c] < moonspos[m2][c]:
                    moonsvel[m1][c] += 1
                    moonsvel[m2][c] -= 1
    for m in range(len(moonspos)):
        moonspos[m][0] += moonsvel[m][0]
        moonspos[m][1] += moonsvel[m][1]
        moonspos[m][2] += moonsvel[m][2]

energy = 0
for moon in range(len(moonspos)):
    pot=abs(moonspos[moon][0])+abs(moonspos[moon][1])+abs(moonspos[moon][2])
    kin=abs(moonsvel[moon][0])+abs(moonsvel[moon][1])+abs(moonsvel[moon][2])
    energy += pot * kin
print(energy)
