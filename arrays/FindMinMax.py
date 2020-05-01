import sys


def lowest(arr):
    first = sys.maxsize
    second = sys.maxsize
    third = sys.maxsize
    for i in range(len(arr)):
        if arr[i] < first:
            third = second
            second = first
            first = arr[i]
        elif arr[i] < second and arr[i] != first:
            second = arr[i]
        elif arr[i] < third and arr[i] != second:
            third = arr[i]

    print(first, second, third)


def greatest(arr):
    first = -100000000
    secon = -10000000
    third = -100000000
    for i in range(len(arr)):
        if arr[i] > first:
            third = secon
            secon = first
            first = arr[i]
        elif arr[i] > secon and arr[i] != first:
            secon = arr[i]
        elif arr[i] > third and arr[i] != secon:
            third = arr[i]

    print(first, secon, third)


array = [10, -6, -6, 12, 3, -20, 14, 8]
lowest(array)
greatest(array)