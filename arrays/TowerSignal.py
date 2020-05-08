towers = [90, 70, 60, 80, 70, 90]
# towers = [12, 100, 40, 60, 120, 90]
newStack = []
size = len(towers)
size = -abs(size)
print(towers)
a = 1
i = -1
while i >= size:
    a = 1
    j = i-1
    while j >= size:
        if towers[i] > towers[j]:
            a = a + 1
        else:
            break
        j -= 1
    newStack.insert(i, a)
    i -= 1

print(newStack)