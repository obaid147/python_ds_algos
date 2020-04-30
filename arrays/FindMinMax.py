import sys


def lowest(arr):
    first = sys.maxsize
    second = sys.maxsize
    for i in range(len(arr)):
        if arr[i] < first:
            second = first
            first = arr[i]
        if arr[i] < second and arr[i] != first:
            second = arr[i]
    print(first, second)


def greatest(arr):
    first = 0
    second = 0
    for i in range(len(arr)):
        if arr[i] > first:
            second = first
            first = arr[i]
        if arr[i] > second and arr[i] != first:
            second = arr[i]
    print(first, second)


array = [10, 2, -6, 12, 3, -20, 14, 8]
lowest(array)
greatest(array)