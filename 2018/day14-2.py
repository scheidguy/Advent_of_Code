
inp = '580741'
digits = len(inp)
recipes = '37'
elf1 = 0
elf2 = 1
while inp != recipes[-digits:] and inp != recipes[-digits-1:-1]:
    if len(recipes) % 10**6 == 0: print(len(recipes))
    r1 = int(recipes[elf1])
    r2 = int(recipes[elf2])
    score = str(r1 + r2)
    recipes += score
    elf1 += 1 + r1
    elf2 += 1 + r2
    elf1 %= len(recipes)
    elf2 %= len(recipes)

print(recipes.index(inp))
