
inp = 580741
recipes = [3, 7]
elf1 = 0
elf2 = 1
while len(recipes) < inp + 10:
    score = str(recipes[elf1] + recipes[elf2])
    for digit in score:
        recipes.append(int(digit))
    elf1 += 1 + recipes[elf1]
    elf2 += 1 + recipes[elf2]
    elf1 %= len(recipes)
    elf2 %= len(recipes)

print(''.join(map(str, recipes[inp:inp+10])))
