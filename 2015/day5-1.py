

f = open('day5_input.txt')
text = f.readlines()
f.close()

vowels = 'aeiou'
nice = 0
for line in text:
    line = line.strip()
    if 'ab' in line or 'cd' in line or 'pq' in line or 'xy' in line: continue
    num = 0
    prev = ''
    double = False
    for letter in line:
        if letter == prev: double = True
        prev = letter
        if letter in vowels: num += 1
    if double and num >= 3: nice += 1
    
print(nice)
