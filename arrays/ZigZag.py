def method1(arr, length, flag):
    a = 0
    for i in range(length):
        a += 1
        if flag:
            x = arr[i+1]
            j =i+1
            if arr[i] > arr[j]:
                arr[j] = arr[i]
                arr[i] = x
            flag = False
        else:
            x = arr[i+1]
            j = i+1
            if arr[i] < arr[j]:
                arr[j] = arr[i]
                arr[i] = x
            flag = True
    return arr


if __name__ == '__main__':
    array = [4, 2, 6, 2, 1, 6, 8, 5]
    size = len(array) - 1
    flag = True
    print(method1(array, size, flag))
# TC O(n) --> SC--> O(1)
def method1(arr):
    length = len(arr) - 1
    flag = True
    for i in range(length):
        j = i + 1
        if flag:
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
            flag = False
        else:
            if arr[i] < arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
            flag = True
    return arr


# If merge sort then TC = O(nlogn) , SC--> O(1)
def method2(arr):
    arr.sort()
    i = 1
    while i < len(arr) - 1:
        if i % 2 != 0:
            j = i + 1
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i = i + 1
        else:
            i = i + 1
    return arr


if __name__ == '__main__':
    array = [4, 2, 6, 1, 5, 8, 3]
    print('Main Array:- ', array)
    # print('ZigZag Array:', method1(array))
    print('Sorted ZigZag Array', method2(array))
