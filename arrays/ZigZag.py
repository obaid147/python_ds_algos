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


# def method2(arr, length):
#     arr.sort()
#     i = 0:
#     while i < len(arr) - 1:
#     i % length !=0
#
#     return arr


if __name__ == '__main__':
    array = [4, 2, 6, 1, 5, 8, 3]
    print('Main Array:- ', array)
    print('ZigZag Array:', method1(array))
    # print('Sorted ZigZag Array', method2(array, size, Flag))
