
from random import randint


def magicmissile(spent, mana, hp):
    spent += spells[0]
    mana -= spells[0]
    hp -= 4
    return spent, mana, hp


def shieldsup(spent, mana):
    spent += spells[1]
    mana -= spells[1]
    shield = 6
    return spent, mana, shield


def poisontime(spent, mana):
    spent += spells[2]
    mana -= spells[2]
    poison = 6
    return spent, mana, poison


def recharging(spent, mana):
    spent += spells[3]
    mana -= spells[3]
    recharge = 5
    return spent, mana, recharge


spells = [53, 113, 173, 229]
damage = 10
wins = []
for simulation in range(10**6):
    hp = 71
    myhp = 50
    myarmor = 0
    mana = 500
    poison = shield = recharge = 0
    spent = 0
    turn = 0
    while myhp > 0 and hp > 0:
        turn += 1
        if turn % 2 == 0:
            if poison > 0:
                hp -= 3
                poison -= 1
            if recharge > 0:
                mana += 101
                recharge -= 1
            if shield > 0:
                myarmor = 7
                shield -= 1
            else: myarmor = 0
    
            dealt = damage - myarmor
            if dealt < 1: dealt = 1
            myhp -= dealt
        else:
            myhp -= 1
            if myhp <= 0: break
            if poison > 0:
                hp -= 3
                poison -= 1
            if recharge > 0:
                mana += 101
                recharge -= 1
            if shield > 0:
                myarmor = 7
                shield -= 1
            else: myarmor = 0
            
            if mana < spells[0]:
                myhp = -1
                break
            elif mana < spells[1]:
                spent, mana, hp = magicmissile(spent, mana, hp)
            elif mana < spells[2]:
                rando = randint(0, 1)
                if rando == 1 and shield == 0: spent, mana, shield = shieldsup(spent, mana)
                else: spent, mana, hp = magicmissile(spent, mana, hp)
            elif mana < spells[3] or mana > 500:
                if shield == 0 and poison == 0:
                    rando = randint(0, 2)
                    if rando == 1: spent, mana, shield = shieldsup(spent, mana)
                    elif rando == 2: spent, mana, poison = poisontime(spent, mana)
                    else: spent, mana, hp = magicmissile(spent, mana, hp)
                elif shield == 0:
                    rando = randint(0, 1)
                    if rando == 1: spent, mana, shield = shieldsup(spent, mana)
                    else: spent, mana, hp = magicmissile(spent, mana, hp)
                elif poison == 0:
                    rando = randint(0, 1)
                    if rando == 1: spent, mana, poison = poisontime(spent, mana)
                    else: spent, mana, hp = magicmissile(spent, mana, hp)
                else:
                    spent, mana, hp = magicmissile(spent, mana, hp)
            else:
                if shield == 0 and poison == 0 and recharge == 0:
                    rando = randint(0, 3)
                    if rando == 1: spent, mana, shield = shieldsup(spent, mana)
                    elif rando == 2: spent, mana, poison = poisontime(spent, mana)
                    elif rando == 3: spent, mana, recharge = recharging(spent, mana)
                    else: spent, mana, hp = magicmissile(spent, mana, hp)
                elif shield == 0 and poison == 0:
                    rando = randint(0, 2)
                    if rando == 1: spent, mana, shield = shieldsup(spent, mana)
                    elif rando == 2: spent, mana, poison = poisontime(spent, mana)
                    else: spent, mana, hp = magicmissile(spent, mana, hp)
                elif recharge == 0 and poison == 0:
                    rando = randint(0, 2)
                    if rando == 1: spent, mana, recharge = recharging(spent, mana)
                    elif rando == 2: spent, mana, poison = poisontime(spent, mana)
                    else: spent, mana, hp = magicmissile(spent, mana, hp)
                elif shield == 0 and recharge == 0:
                    rando = randint(0, 2)
                    if rando == 1: spent, mana, shield = shieldsup(spent, mana)
                    elif rando == 2: spent, mana, recharge = recharging(spent, mana)
                    else: spent, mana, hp = magicmissile(spent, mana, hp)
                elif poison == 0:
                    rando = randint(0, 1)
                    if rando == 1: spent, mana, poison = poisontime(spent, mana)
                    else: spent, mana, hp = magicmissile(spent, mana, hp)
                elif shield == 0:
                    rando = randint(0, 1)
                    if rando == 1: spent, mana, shield = shieldsup(spent, mana)
                    else: spent, mana, hp = magicmissile(spent, mana, hp)
                elif recharge == 0:
                    rando = randint(0, 1)
                    if rando == 1: spent, mana, recharge = recharging(spent, mana)
                    else: spent, mana, hp = magicmissile(spent, mana, hp)
                else:
                    spent, mana, hp = magicmissile(spent, mana, hp)
    
    if hp <= 0: wins.append(spent)

print(min(wins))
