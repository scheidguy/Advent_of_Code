
tape = [0 for _ in range(10**6)]
pos = 10**6//2

state = 'a'
for step in range(12368930):
    if state == 'a':
        if tape[pos]:
            tape[pos] = 0
            pos += 1
            state = 'c'
        else:
            tape[pos] = 1
            pos += 1
            state = 'b'
    elif state == 'b':
        if tape[pos]:
            tape[pos] = 0
            pos += 1
            state = 'd'
        else:
            tape[pos] = 0
            pos -= 1
            state = 'a'
    elif state == 'c':
        if tape[pos]:
            tape[pos] = 1
            pos += 1
            state = 'a'
        else:
            tape[pos] = 1
            pos += 1
            state = 'd'
    elif state == 'd':
        if tape[pos]:
            tape[pos] = 0
            pos -= 1
            state = 'd'
        else:
            tape[pos] = 1
            pos -= 1
            state = 'e'
    elif state == 'e':
        if tape[pos]:
            tape[pos] = 1
            pos -= 1
            state = 'b'
        else:
            tape[pos] = 1
            pos += 1
            state = 'f'
    elif state == 'f':
        if tape[pos]:
            tape[pos] = 1
            pos += 1
            state = 'e'
        else:
            tape[pos] = 1
            pos += 1
            state = 'a'

print(sum(tape))
