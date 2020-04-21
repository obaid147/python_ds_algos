def count1(array, size, checkerArray):
    for i in range(size):
        count = 1
        if checkerArray[i]:
            continue
        for j in range(i + 1, size):
            if array[i] == array[j]:
                checkerArray[j] = True
                count += 1
        print(array[i], '->', count)


def count_dict(arr, n):
    mp = dict()
    for i in range(n):
        if arr[i] in mp.keys():
            mp[arr[i]] += 1
        else:
            mp[arr[i]] = 1

    for i in mp:
        print(i, " ", mp[i])


arr = [4, 2, 6, 1, 4, 1, 6]
checker = [False, False, False, False, False, False, False]
n = len(arr)
count1(arr, n, checker)
count_dict(arr, n)