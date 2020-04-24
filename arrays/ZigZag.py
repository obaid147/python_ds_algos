def method1(arr, length, flag):
    for i in range(length):
        x = arr[i]
        j = i + 1
        if flag:
            if arr[i] > arr[j]:
                arr[i] = arr[j]
                arr[j] = x
            flag = False
        else:
            if arr[i] < arr[j]:
                arr[i] = arr[j]
                arr[j] = x
            flag = True
    return arr


def method2(arr, length, flag):
    arr.sort()
    for i in range(length):
        x = arr[i]
        j = i + 1
        if flag:
            if arr[i] > arr[j]:
                arr[i] = arr[j]
                arr[j] = x
            flag = False
        else:
            if arr[i] < arr[j]:
                arr[i] = arr[j]
                arr[j] = x
            flag = True
    return arr


array = [4, 2, 6, 1, 5, 8, 3]
print('Main Array:- ', array)
size = len(array) - 1
Flag = True
# print('ZigZag Array:', method1(array, length, flag))
print('Sorted ZigZag Array', method1(array, size, Flag))
