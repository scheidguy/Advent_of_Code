
start = 289326
manhattan1 = (start**0.5 - 1)//2 + 1
remainder = start - int(start**0.5)**2
print(manhattan1 + (remainder % int(start**0.5)) - (int(start**0.5)+1)//2 - 1)
