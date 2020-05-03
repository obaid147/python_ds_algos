def perfectArray(array):
    i = 0
    j = len(arr) - 1
    while i < j:
        if array[i] != array[j]:
            return 'Not Perfect'
        else:
            i = i + 1
            j = j - 1
    return 'Perfect'


if __name__ == '__main__':
    arr = [1, 21, 3, 2, 1]
    print(perfectArray(arr))