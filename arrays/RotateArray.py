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


def gdc(n1, n2):
    if not n2:
        return n1
    else:
        return gdc(n2, n1 % n2)


def jugglingMethod1(n, d, array):
    for i in range(gdc(n, d)):
        temp = array[i]
        j = i
        while True:
            k = j + d
            if k >= n:
                k = k - n
            if k == i:
                break
            array[j] = array[k]
            j = k
        array[j] = temp


def jugglingMethod2(n, d, array):
    for i in range(gdc(n, d)):
        temp = array[i]
        j = i
        while True:
            k = (j + d) % n
            if k == i:
                break
            array[j] = array[k]
            j = k
        array[j] = temp


array1 = [1, 2, 3, 4, 5, 6]
array2 = [1, 2, 3, 4, 5]
size = len(array2)
num = int(input("Enter indices to rotate: "))
if num > size:
    print("Index Error")
    exit(1)

print("Current array ", array2)
# jugglingMethod1(size, num, array)
jugglingMethod2(size, num, array2)
print('Rotated Array', array2)