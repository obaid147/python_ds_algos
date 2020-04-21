#               Method1
#           Time complexity --> O(n^2) ; aux-space O(n*d)

#               Method2
#           Time complexity --> O(n) ; aux-space O(d)


def sort(arrayElements2, new_list):
    while arrayElements2:
        min = arrayElements2[0]
        for x in arrayElements2:
            if x < min:
                min = x
        new_list.append(min)
        arrayElements2.remove(min)


def Method1(array, num, new_list):
    sort(array, new_list)
    index = 0
    length = len(new_list) - 1
    print(new_list)
    while index < length:
        if new_list[index] + new_list[length] == num:
            return new_list[index], new_list[length]
        elif new_list[index] + new_list[length] < num:
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
new_list = []
n = 10
print(Method1(arrayElements2, n, new_list))
n = 16
arrayElements1 = [1, 4, 45, 6, 10, 8]
print(Method2(arrayElements1, len(arrayElements1), n))