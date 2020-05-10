# towers = [90, 70, 60, 80, 70, 90]
towers = [12, 100, 40, 60, 120, 90]
newStack = []
size = len(towers)
size = -abs(size)
print(towers)

count = 1
newStack.append(count)
for i in range(1, len(towers)):
    count = 1
    j = i - 1
    while j >= 0:
        if towers[i] <= towers[j]:
            break
        else:
            count += 1
        j -= 1
    newStack.append(count)
print(newStack)