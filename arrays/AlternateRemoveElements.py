def removeElements(arr):
    size = len(arr)
    for i in range(size):
        if len(arr) == 1:
            return arr
        if i & 1 == 0:
            arr.remove(max(arr))
        elif i & 1 == 1:
            arr.remove(min(arr))

def usingSort(arr):
    n = len(arr)
    arr.sort()
    div = n // 2
    if n % 2  == 0:
        return arr[n // 2 - 1]
    else:
        return arr[n //2]
# array = [7, 8, 3, 4, 2, 9, 5]
array = [2, 1, -2, 8, 5, 3, 4, 9]


print(removeElements(array))
print(usingSort(array))
