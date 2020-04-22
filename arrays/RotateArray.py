def reverseArray(array, start, end):
    while start < end:
        temp = array[start]
        array[start] = array[end]
        array[end] = temp
        start += 1
        end -= 1


def method3(array, d):
    if d == 0:
        return
    n = len(array)
    reverseArray(array, 0, d - 1)
    reverseArray(array, d, n - 1)
    reverseArray(array, 0, n - 1)


#               Method2
#       Time complexity --> O(n*rotateBy)
def method2(array, rotateBy):
    for i in range(rotateBy):
        rotate2(array)


def rotate2(array):
    temp = array[0]
    for i in range(len(array)-1):
        array[i] = array[i+1]
    array[-1] = temp


#               Method1
#       Time complexity --> O(n) ; aux-space --> O(rotateby) --> O(no of rotations.)
def method1(arr, rotateBy):
    newArray = []
    for i in range(len(arr)):
        if i < rotateBy:
            newArray.append(arr[i])
        else:
            arr[i - rotateBy] = arr[i]

    for i in range(rotateBy):
        if rotateBy == 7:
            break
        arr[len(arr) - (rotateBy - i)] = newArray[i]


array = [1, 2, 3, 4, 5, 6, 7]
n = int(input("Enter indices to rotate: "))
print("Current array ", array)
method3(array, n)
print('Rotated Array', array)