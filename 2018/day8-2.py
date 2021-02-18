

def processnodes(tree):
    numchild = tree.pop(0)
    nummeta = tree.pop(0)
    values = []
    for child in range(numchild):
        vals, tree = processnodes(tree)
        values.append(vals)
    numvals = len(values)
    for meta in range(nummeta):
        if numchild == 0:
            values.append(tree.pop(0))
        else:
            ind = tree.pop(0) - 1
            if ind < numvals:
                values.append(values[ind])
    if numchild != 0:
        for _ in range(numvals):
            values.pop(0)
    return sum(values), tree


f = open('day8_input.txt')
text = f.readlines()
f.close()

for line in text:
    line = line.strip().split()
    tree = list(map(int, line))

values, tree = processnodes(tree)
print(values)
