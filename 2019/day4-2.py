
howmany = 0
for num in range(264793, 803935 + 1):
    n = str(num)
    if any([n[0]==n[1] and n[1]!=n[2], n[1]==n[2] and n[2]!=n[3] and n[0]!=n[1], n[2]==n[3] and n[3]!=n[4] and n[1]!=n[2], n[3]==n[4] and n[4]!=n[5] and n[2]!=n[3], n[4]==n[5] and n[3]!=n[4]]):
        if n[0]<=n[1] and n[1]<=n[2] and n[2]<=n[3] and n[3]<=n[4] and n[4]<=n[5]:
            howmany += 1
print(howmany)
