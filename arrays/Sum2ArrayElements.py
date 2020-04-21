#               Method1
#           Time complexity --> O(n) ; aux-space O(n)

#               Method2
#           Time complexity --> O(n) ;


def Method1(array, num):
    array.sort()
    index = 0
    length = len(array) - 1
    while index < length:
        if array[index] + array[length] == num:
            return array[index], array[length]
        elif array[index] + array[length] < num:
            index += 1
        else:
            length -= 1
    return -1, -1


def Method2(array, arr_size, num):
    set1 = set()
    for i in range(arr_size):
        element = num - array[i]
        if element in set1:
            return array[i], element
        set1.add(array[i])
    return -1


arrayElements2 = [1, 6, 3, 9, 4]
n = 10
print(Method1(arrayElements2, n))
n = 16
arrayElements1 = [1, 4, 45, 6, 10, 8]
print(Method2(arrayElements1, len(arrayElements1), n))