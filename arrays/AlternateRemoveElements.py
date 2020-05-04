def removeElements(arr):
    size = len(arr)
    for i in range(size):
        if len(arr) == 1:
            return arr
        if i & 1 == 0:
            arr.remove(max(arr))
        elif i & 1 == 1:
            arr.remove(min(arr))


# array = [7, 8, 3, 4, 2, 9, 5]
array = [8, 1, 2, 9, 4, 3, 7, 5]
print(removeElements(array))