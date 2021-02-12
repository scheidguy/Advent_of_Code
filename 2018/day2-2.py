
f = open('day2_input.txt')
text = f.readlines()
f.close()

boxes = []
for line in text:
    line = line.strip()
    line = list(line)
    for box in boxes:
        mismatches = 0
        for i in range(len(line)):
            if box[i] != line[i]:
                mismatches += 1
        if mismatches == 1:
            print(''.join(line))
            print(''.join(box))
    boxes.append(line)
