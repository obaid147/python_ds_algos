# sum of two array elements to n 1
def sumElementsArray1(array, num):
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


# sum of two array elements to n TWO
def sumElementsArraySet(array, arr_size, num):
    # [1, 4, 45, 6, 10, 8]
    # num = 16
    # set1.add =(1, 4, 45, 6, (16-10) is in set return)
    set1 = set()
    for i in range(arr_size):
        element = num - array[i]
        if element in set1:
            return array[i], element
        set1.add(array[i])
    return -1


n = 10
arrayElements2 = [1, 6, 3, 9, 4]

new_list = []
while arrayElements2:
    min = arrayElements2[0]
    for x in arrayElements2:
        if x < min:
            min = x
    new_list.append(min)
    arrayElements2.remove(min)
    # print(sumElementsArray1(new_list, n))
print("---------------------Sum ARRAY Elements case 2 ------------")
n = 16
arrayElements1 = [1, 4, 45, 6, 10, 8]
print(sumElementsArraySet(arrayElements1, len(arrayElements1), n))