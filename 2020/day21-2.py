
f = open('day21-1_input.txt')
# f = open('day21-1_debug.txt')
text = f.readlines()
f.close()

allergens = {}
allingredients = []
for food in text:
    food = food.split('(')
    ingredients = food[0].split()
    allingredients.extend(ingredients)
    contains = food[1].split()[1:]
    for i in range(len(contains)):
        contains[i] = contains[i][0:-1]  # remove commas and ) at end of line
    for c in contains:
        if c not in allergens.keys():
            allergens[c] = set(ingredients)
        else:
            ingred = set(ingredients)
            allergens[c] = allergens[c].intersection(ingred)
            
for key in allergens.keys():
    candidates = list(allergens[key])
    for cand in candidates:
        while cand in allingredients: allingredients.remove(cand)

updated = True
canon = []
while updated:
    updated = False
    for key in allergens.keys():
        if len(allergens[key]) == 1:
            found = list(allergens[key])[0]
            for key2 in allergens.keys():
                if key2 == key: continue
                if found in allergens[key2]:
                    allergens[key2].remove(found)
                    updated = True

allerglist = list(allergens.keys())
allerglist.sort()
canon = [allergens[a].pop() for a in allerglist]


# print(len(allingredients))
print(','.join(canon))

