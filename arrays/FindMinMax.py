def Greatest(arr):
    greatest = arr[0]
    for i in arr:
        if i > greatest:
            greatest = i
    print('Greatest = ', greatest)

    secGreatest = arr[0]
    arr.remove(max(arr))
    for i in arr:
        if i > secGreatest:
            secGreatest = i
    print('Second Greatest = ', secGreatest)


def Lowest(arr):
    lowest = arr[0]
    for i in arr:
        if i < lowest:
            lowest = i
    print('Lowest = ', lowest)

    arr.remove((min(arr)))
    low = arr[0]
    for i in arr:
        if i < low:
            low = i
    print('Second Lowest = ', low)


if __name__ == '__main__':
    array = [100, 500, 900, 760, 800, 300]
    Greatest(array)
    # Lowest(array)