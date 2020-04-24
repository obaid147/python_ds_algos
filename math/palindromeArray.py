def method1(array, j, flag, i):
    while i < j:
        if array[i] == array[j]:
            i = i + 1
            j = j - 1
            flag = True
        else:
            flag = False
            break
    if flag:
        print(array, 'is Palindrome')
    else:
        print(array, 'is  not Palindrome')


if __name__ == '__main__':
    arr = [1, 2, 4, 2, 1]
    size = len(arr) - 1
    flag1 = True
    method1(arr, size, flag1, i=0)
