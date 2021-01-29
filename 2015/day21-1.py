
damage = 9
armor = 2
weapons = [(8,4), (10,5), (25,6), (40,7), (74,8)]
armors = [(0,0), (13,1), (31,2), (53,3), (75,4), (102,5)]
rings1 = [(0,0,0), (25,1,0), (50,2,0), (100,3,0), (20,0,1), (40,0,2), (80,0,3)]
rings2 = [(0,0,0), (25,1,0), (50,2,0), (100,3,0), (20,0,1), (40,0,2), (80,0,3)]

cheapest = 10**6
for weapon in weapons:
    for arm in armors:
        for ring1 in rings1:
            for ring2 in rings2:
                mydamage = weapon[1] + ring1[1] + ring2[1]
                myarmor = arm[1] + ring1[2] + ring2[2]
                spent = weapon[0] + arm[0] + ring1[0] + ring2[0]
                myhp = 100
                hp = 103
                won = False
                while myhp > 0:
                    dealt = mydamage - armor
                    if dealt < 1: dealt = 1
                    hp -= dealt
                    if hp <= 0: won = True
                    dealt = damage - myarmor
                    if dealt < 1: dealt = 1
                    myhp -= dealt
                if won:
                    if spent < cheapest: cheapest = spent
print(cheapest)
