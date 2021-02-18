

def processnodes(tree):
    metadata = 0
    numchild = tree.pop(0)
    nummeta = tree.pop(0)
    for child in range(numchild):
        met, tree = processnodes(tree)
        metadata += met
    for meta in range(nummeta):
        metadata += tree.pop(0)
    return metadata, tree


f = open('day8_input.txt')
text = f.readlines()
f.close()

for line in text:
    line = line.strip().split()
    tree = list(map(int, line))

metadata, tree = processnodes(tree)
print(metadata)
