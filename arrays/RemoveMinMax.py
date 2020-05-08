import sys


def mainMethod(arr):
    length = len(arr)
    for i in range(length):
        if len(arr) == 1:
            return arr
        if i % 2 == 0:
            arr.remove(greatest(arr))
            # arr.remove(max(arr)
        else:
            arr.remove(lowest(arr))
            # arr.remove(min(arr))
    return arr


def lowest(arr):
    first = sys.maxsize
    for i in range(len(arr)):
        if arr[i] < first:
            first = arr[i]
    return first


def greatest(arr):
    first = -1000000
    for i in range(len(arr)):
        if arr[i] > first:
            first = arr[i]
    return first


if __name__ == '__main__':
    # array = [7, 8, 3, 4, 2, 9, 5]
    array = [8, 1, 2, 9, 4, 3, 7, 5]
    print(mainMethod(array))
