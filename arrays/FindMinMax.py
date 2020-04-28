def maxMin(arr):
    # TC--> O(n)
    gr8 = arr[0]
    for i in arr:
        if i > gr8:
            gr8 = i
    print('Highest = ', gr8)

    # TC--> O(n)
    low = arr[0]
    for i in arr:
        if i < low:
            low = i
    print('Lowest = ', low)


def secondMaxMin(arr):
    # ===2nd Highest/lowest======
    arr.remove(max(arr))
    gr8 = arr[0]
    for i in arr:
        if i > gr8:
            gr8 = i
    print('2nd Highest = ', gr8)

    arr.remove((min(arr)))
    low = arr[0]
    for i in arr:
        if i < low:
            low = i
    print('2nd Lowest = ', low)


def thirdMaxMin(arr):
    # ===2nd Highest/lowest======
    arr.remove(max(arr))
    arr.remove(max(arr))
    gr8 = arr[0]
    for i in arr:
        if i > gr8:
            gr8 = i
    print('3rd Highest = ', gr8)

    arr.remove((min(arr)))
    arr.remove((min(arr)))
    low = arr[0]
    for i in arr:
        if i < low:
            low = i
    print('3rd Lowest = ', low)


if __name__ == '__main__':
    array = [1, 3, 5, 7, 9, 2]
    maxMin(array)
    secondMaxMin(array)
    # thirdMaxMin(array)